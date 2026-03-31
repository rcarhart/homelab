from functools import cached_property

from fastapi import HTTPException, status
from pydantic import UUID4

from mealie.routes._base import BaseUserController, controller
from mealie.routes._base.mixins import HttpRepo
from mealie.routes._base.routers import MealieCrudRoute, UserAPIRouter
from mealie.schema.recipe import Recipe
from mealie.schema.response.responses import ErrorResponse
from mealie.schema.shared import (
    SharedRecipeCollectionCreate,
    SharedRecipeCollectionOut,
    SharedRecipeCollectionSave,
    SharedRecipeCollectionUpdate,
    SharedRecipeCopyRequest,
    SharedRecipeLinkCreate,
    SharedRecipeLinkOut,
)
from mealie.services.shared_collection_service import SharedCollectionService

router = UserAPIRouter(prefix="/shared-collections", tags=["Shared Collections"], route_class=MealieCrudRoute)


@controller(router)
class SharedCollectionsController(BaseUserController):
    @cached_property
    def repo(self):
        return self.repos.shared_recipe_collections

    @cached_property
    def link_repo(self):
        return self.repos.shared_recipe_links

    @cached_property
    def mixins(self):
        return HttpRepo[SharedRecipeCollectionSave, SharedRecipeCollectionOut, SharedRecipeCollectionUpdate](
            self.repo,
            self.logger,
        )

    @cached_property
    def service(self):
        return SharedCollectionService(self.repos, self.user, self.household, self.translator)

    @router.get("", response_model=list[SharedRecipeCollectionOut])
    def get_all(self):
        return self.service.visible_collections()

    @router.post("", response_model=SharedRecipeCollectionOut, status_code=201)
    def create_one(self, data: SharedRecipeCollectionCreate):
        save_data = self.service.build_collection_save(data)
        collection = self.mixins.create_one(save_data)
        if collection is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, ErrorResponse.respond(message="Unable to create"))

        owner_membership = self.service.build_owner_membership(collection.id)
        self.repos.shared_recipe_collection_members.create(owner_membership)
        return self.service.get_collection(collection.id)

    @router.get("/{item_id}", response_model=SharedRecipeCollectionOut)
    def get_one(self, item_id: UUID4):
        return self.service.assert_view_access(item_id)

    @router.put("/{item_id}", response_model=SharedRecipeCollectionOut)
    def update_one(self, item_id: UUID4, data: SharedRecipeCollectionCreate):
        existing = self.service.assert_manage_access(item_id)
        update_data = SharedRecipeCollectionUpdate(
            id=item_id,
            owner_user_id=existing.owner_user_id,
            origin_group_id=existing.origin_group_id,
            origin_household_id=existing.origin_household_id,
            **data.model_dump(),
        )
        return self.mixins.update_one(update_data, item_id)

    @router.delete("/{item_id}", response_model=SharedRecipeCollectionOut)
    def delete_one(self, item_id: UUID4):
        self.service.assert_manage_access(item_id)
        return self.mixins.delete_one(item_id)

    @router.get("/{item_id}/recipes", response_model=list[SharedRecipeLinkOut])
    def list_recipes(self, item_id: UUID4):
        return self.service.list_collection_recipes(item_id)

    @router.post("/{item_id}/recipes", response_model=SharedRecipeLinkOut, status_code=201)
    def add_recipe(self, item_id: UUID4, data: SharedRecipeLinkCreate):
        payload = self.service.validate_link_payload(item_id, data)
        return self.link_repo.create(payload)

    @router.delete("/{item_id}/recipes/{recipe_id}", response_model=SharedRecipeLinkOut)
    def remove_recipe(self, item_id: UUID4, recipe_id: UUID4):
        self.service.assert_manage_access(item_id)
        link = self.service.get_collection_recipe_link(item_id, recipe_id)
        if not link:
            raise HTTPException(status.HTTP_404_NOT_FOUND, ErrorResponse.respond(message="Not found."))
        return self.link_repo.delete(link.id)

    @router.post("/{item_id}/recipes/{recipe_id}/copy", response_model=Recipe, status_code=201)
    def copy_recipe_to_household(self, item_id: UUID4, recipe_id: UUID4, data: SharedRecipeCopyRequest):
        return self.service.copy_recipe_to_household(item_id, recipe_id, data)
