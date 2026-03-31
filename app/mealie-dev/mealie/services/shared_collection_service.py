from __future__ import annotations

from shutil import copytree
from uuid import UUID

from fastapi import HTTPException, status
from slugify import slugify

from mealie.repos.all_repositories import get_repositories
from mealie.repos.repository_factory import AllRepositories
from mealie.schema.recipe import Recipe
from mealie.schema.recipe.recipe import RecipeSummary
from mealie.schema.response.responses import ErrorResponse
from mealie.schema.shared import (
    SharedRecipeCollectionCreate,
    SharedRecipeCollectionMemberCreate,
    SharedRecipeCollectionMemberOut,
    SharedRecipeCollectionOut,
    SharedRecipeCollectionSave,
    SharedRecipeCommentCreate,
    SharedRecipeCopyRequest,
    SharedRecipeLinkCreate,
)
from mealie.schema.user.user import PrivateUser
from mealie.services.recipe.recipe_data_service import RecipeDataService
from mealie.services.recipe.recipe_service import RecipeService


class SharedCollectionService:
    def __init__(self, repos: AllRepositories, user: PrivateUser, household, translator):
        self.repos = repos
        self.user = user
        self.household = household
        self.translator = translator
        self.group_repos = get_repositories(repos.session, group_id=user.group_id, household_id=None)

    def _error(self, status_code: int, message: str) -> HTTPException:
        return HTTPException(status_code, ErrorResponse.respond(message=message))

    def build_collection_save(self, data: SharedRecipeCollectionCreate) -> SharedRecipeCollectionSave:
        return SharedRecipeCollectionSave(
            **data.model_dump(),
            slug=data.slug or slugify(data.name),
            owner_user_id=self.user.id,
            origin_group_id=self.user.group_id,
            origin_household_id=self.user.household_id,
        )

    def build_owner_membership(self, collection_id):
        return SharedRecipeCollectionMemberCreate(
            collection_id=collection_id,
            user_id=self.user.id,
            role="owner",
            can_comment=True,
            can_copy=True,
        )

    def get_collection(self, collection_id) -> SharedRecipeCollectionOut:
        collection = self.group_repos.shared_recipe_collections.get_one(collection_id)
        if not collection:
            raise self._error(status.HTTP_404_NOT_FOUND, "Collection not found")
        return collection

    def get_membership(self, collection_id, user_id=None) -> SharedRecipeCollectionMemberOut | None:
        memberships = self.repos.shared_recipe_collection_members.multi_query(
            {"collection_id": collection_id, "user_id": user_id or self.user.id},
            limit=1,
        )
        return memberships[0] if memberships else None

    def visibility_allows(self, collection: SharedRecipeCollectionOut) -> bool:
        if collection.owner_user_id == self.user.id:
            return True

        membership = self.get_membership(collection.id)
        if membership:
            return True

        if collection.visibility_mode == "group":
            return True

        if collection.visibility_mode == "household":
            return collection.origin_household_id == self.user.household_id

        return False

    def assert_view_access(self, collection_id) -> SharedRecipeCollectionOut:
        collection = self.get_collection(collection_id)
        if not self.visibility_allows(collection):
            raise self._error(status.HTTP_403_FORBIDDEN, "You do not have access to this collection")
        return collection

    def assert_manage_access(self, collection_id) -> SharedRecipeCollectionOut:
        collection = self.get_collection(collection_id)
        membership = self.get_membership(collection_id)
        if collection.owner_user_id != self.user.id or not membership or membership.role != "owner":
            raise self._error(status.HTTP_403_FORBIDDEN, "Only collection owners can perform this action")
        return collection

    def assert_comment_access(self, collection_id) -> SharedRecipeCollectionOut:
        collection = self.assert_view_access(collection_id)
        if not collection.allow_comments:
            raise self._error(status.HTTP_403_FORBIDDEN, "Comments are disabled for this collection")

        membership = self.get_membership(collection_id)
        if membership and membership.can_comment:
            return collection
        if collection.owner_user_id == self.user.id:
            return collection
        if collection.visibility_mode in {"group", "household"}:
            return collection

        raise self._error(status.HTTP_403_FORBIDDEN, "You do not have permission to comment in this collection")

    def assert_copy_access(self, collection_id) -> SharedRecipeCollectionOut:
        collection = self.assert_view_access(collection_id)
        if not collection.allow_copy:
            raise self._error(status.HTTP_403_FORBIDDEN, "Copying is disabled for this collection")

        membership = self.get_membership(collection_id)
        if membership and membership.can_copy:
            return collection
        if collection.owner_user_id == self.user.id:
            return collection
        if collection.visibility_mode in {"group", "household"}:
            return collection

        raise self._error(status.HTTP_403_FORBIDDEN, "You do not have permission to copy from this collection")

    def visible_collections(self) -> list[SharedRecipeCollectionOut]:
        collections = self.group_repos.shared_recipe_collections.get_all()
        return [collection for collection in collections if self.visibility_allows(collection)]

    def validate_member_payload(self, collection_id, data: SharedRecipeCollectionMemberCreate):
        self.assert_manage_access(collection_id)
        if data.collection_id != collection_id:
            raise self._error(status.HTTP_400_BAD_REQUEST, "Collection mismatch")
        if data.role not in {"owner", "member"}:
            raise self._error(status.HTTP_400_BAD_REQUEST, "Invalid collection member role")
        user = self.group_repos.users.get_one(data.user_id)
        if not user:
            raise self._error(status.HTTP_404_NOT_FOUND, "User not found")
        return SharedRecipeCollectionMemberCreate(
            collection_id=collection_id,
            user_id=data.user_id,
            role=data.role,
            can_comment=data.can_comment,
            can_copy=data.can_copy,
        )

    def validate_link_payload(self, collection_id, data: SharedRecipeLinkCreate):
        self.assert_manage_access(collection_id)
        if data.collection_id != collection_id:
            raise self._error(status.HTTP_400_BAD_REQUEST, "Collection mismatch")
        recipe = self.group_repos.recipes.get_one(data.recipe_id, key="id", override_schema=RecipeSummary)
        if not recipe:
            raise self._error(status.HTTP_404_NOT_FOUND, "Recipe not found")
        return SharedRecipeLinkCreate(
            collection_id=collection_id,
            recipe_id=data.recipe_id,
            shared_by_user_id=self.user.id,
        )

    def validate_comment_payload(self, collection_id, recipe_id, data: SharedRecipeCommentCreate):
        self.assert_comment_access(collection_id)
        if data.collection_id != collection_id or data.recipe_id != recipe_id:
            raise self._error(status.HTTP_400_BAD_REQUEST, "Context mismatch")
        link = self.get_collection_recipe_link(collection_id, recipe_id)
        if not link:
            raise self._error(status.HTTP_404_NOT_FOUND, "Recipe is not shared in this collection")
        return SharedRecipeCommentCreate(
            collection_id=collection_id,
            recipe_id=recipe_id,
            user_id=self.user.id,
            text=data.text,
        )

    def get_collection_recipe_link(self, collection_id, recipe_id):
        links = self.repos.shared_recipe_links.multi_query({"collection_id": collection_id, "recipe_id": recipe_id}, limit=1)
        return links[0] if links else None

    def list_collection_recipes(self, collection_id):
        self.assert_view_access(collection_id)
        return self.repos.shared_recipe_links.multi_query({"collection_id": collection_id}, order_by="created_at")

    def copy_recipe_to_household(self, collection_id, recipe_id: UUID | str, payload: SharedRecipeCopyRequest):
        self.assert_copy_access(collection_id)
        link = self.get_collection_recipe_link(collection_id, recipe_id)
        if not link:
            raise self._error(status.HTTP_404_NOT_FOUND, "Recipe is not shared in this collection")

        source_recipe = self.group_repos.recipes.get_one(recipe_id, key="id", override_schema=Recipe)
        if not source_recipe:
            raise self._error(status.HTTP_404_NOT_FOUND, "Recipe not found")

        recipe_service = RecipeService(self.repos, self.user, self.household, translator=self.translator)
        source_dump = source_recipe.model_dump(exclude={"id", "slug", "comments", "created_at", "updated_at"}, round_trip=True)
        source_dump["name"] = payload.name or source_recipe.name or "Copied Recipe"
        source_dump["source_recipe_id"] = source_recipe.id
        source_dump["is_household_copy"] = True
        source_dump["user_id"] = self.user.id
        source_dump["household_id"] = self.user.household_id
        source_dump["group_id"] = self.user.group_id
        copied_recipe = recipe_service.create_one(Recipe.model_validate(source_dump))

        try:
            copytree(RecipeDataService(source_recipe.id).dir_data, RecipeDataService(copied_recipe.id).dir_data, dirs_exist_ok=True)
        except Exception:
            pass

        model = self.repos.session.get(self.repos.recipes.model, copied_recipe.id)
        if model is not None:
            model.source_recipe_id = source_recipe.id
            model.is_household_copy = True
            self.repos.session.commit()
            self.repos.session.refresh(model)

        return self.repos.recipes.get_one(copied_recipe.id, key="id", override_schema=Recipe)
