from slugify import slugify

from mealie.repos.repository_factory import AllRepositories
from mealie.schema.shared import (
    SharedRecipeCollectionCreate,
    SharedRecipeCollectionMemberCreate,
    SharedRecipeCollectionSave,
    SharedRecipeCommentCreate,
    SharedRecipeLinkCreate,
)
from mealie.schema.user.user import PrivateUser


class SharedCollectionService:
    def __init__(self, repos: AllRepositories, user: PrivateUser):
        self.repos = repos
        self.user = user

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

    def assert_collection_owner(self, collection_id):
        membership = self.repos.shared_recipe_collection_members.get_one(collection_id, key="collection_id")
        if not membership or membership.user_id != self.user.id or membership.role != "owner":
            raise PermissionError("Only collection owners can perform this action")
        return membership

    def validate_member_payload(self, data: SharedRecipeCollectionMemberCreate):
        if data.role not in {"owner", "member"}:
            raise ValueError("Invalid collection member role")
        return data

    def validate_link_payload(self, data: SharedRecipeLinkCreate):
        recipe = self.repos.recipes.get_one(data.recipe_id, key="id")
        if not recipe:
            raise ValueError("Recipe not found")
        return data

    def validate_comment_payload(self, data: SharedRecipeCommentCreate):
        collection = self.repos.shared_recipe_collections.get_one(data.collection_id)
        if not collection:
            raise ValueError("Collection not found")
        recipe = self.repos.recipes.get_one(data.recipe_id, key="id")
        if not recipe:
            raise ValueError("Recipe not found")
        return data
