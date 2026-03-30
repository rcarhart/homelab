from functools import cached_property

from fastapi import APIRouter, HTTPException, status
from pydantic import UUID4

from mealie.routes._base import BaseUserController, controller
from mealie.routes._base.mixins import HttpRepo
from mealie.routes._base.routers import MealieCrudRoute, UserAPIRouter
from mealie.schema.response.responses import ErrorResponse
from mealie.schema.shared import (
    SharedRecipeCollectionCreate,
    SharedRecipeCollectionOut,
    SharedRecipeCollectionPagination,
    SharedRecipeCollectionSave,
    SharedRecipeCollectionUpdate,
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
        return SharedCollectionService(self.repos, self.user)

    @router.get("", response_model=list[SharedRecipeCollectionOut])
    def get_all(self):
        return self.repo.get_all()

    @router.post("", response_model=SharedRecipeCollectionOut, status_code=201)
    def create_one(self, data: SharedRecipeCollectionCreate):
        save_data = self.service.build_collection_save(data)
        collection = self.mixins.create_one(save_data)
        if collection is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, ErrorResponse.respond(message="Unable to create"))

        owner_membership = self.service.build_owner_membership(collection.id)
        self.repos.shared_recipe_collection_members.create(owner_membership)
        return self.repo.get_one(collection.id)

    @router.get("/{item_id}", response_model=SharedRecipeCollectionOut)
    def get_one(self, item_id: UUID4):
        return self.mixins.get_one(item_id)

    @router.put("/{item_id}", response_model=SharedRecipeCollectionOut)
    def update_one(self, item_id: UUID4, data: SharedRecipeCollectionCreate):
        existing = self.repo.get_one(item_id)
        if not existing:
            raise HTTPException(status.HTTP_404_NOT_FOUND, ErrorResponse.respond(message="Not found."))

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
        return self.mixins.delete_one(item_id)

    @router.post("/{item_id}/recipes", response_model=SharedRecipeLinkOut, status_code=201)
    def add_recipe(self, item_id: UUID4, data: SharedRecipeLinkCreate):
        if data.collection_id != item_id:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, ErrorResponse.respond(message="Collection mismatch"))
        payload = self.service.validate_link_payload(data)
        return self.link_repo.create(payload)
