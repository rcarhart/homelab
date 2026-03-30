from functools import cached_property

from fastapi import HTTPException, status
from pydantic import UUID4

from mealie.routes._base import BaseUserController, controller
from mealie.routes._base.mixins import HttpRepo
from mealie.routes._base.routers import UserAPIRouter
from mealie.schema.response.responses import ErrorResponse
from mealie.schema.shared import SharedRecipeCollectionMemberCreate, SharedRecipeCollectionMemberOut
from mealie.services.shared_collection_service import SharedCollectionService

router = UserAPIRouter(prefix="/shared-collections/{collection_id}/members", tags=["Shared Collection Members"])


@controller(router)
class SharedCollectionMembersController(BaseUserController):
    @cached_property
    def repo(self):
        return self.repos.shared_recipe_collection_members

    @cached_property
    def mixins(self):
        return HttpRepo[SharedRecipeCollectionMemberCreate, SharedRecipeCollectionMemberOut, SharedRecipeCollectionMemberCreate](
            self.repo,
            self.logger,
        )

    @cached_property
    def service(self):
        return SharedCollectionService(self.repos, self.user)

    @router.get("", response_model=list[SharedRecipeCollectionMemberOut])
    def get_all(self, collection_id: UUID4):
        return self.repo.multi_query({"collection_id": collection_id})

    @router.post("", response_model=SharedRecipeCollectionMemberOut, status_code=201)
    def create_one(self, collection_id: UUID4, data: SharedRecipeCollectionMemberCreate):
        if data.collection_id != collection_id:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, ErrorResponse.respond(message="Collection mismatch"))
        payload = self.service.validate_member_payload(data)
        return self.mixins.create_one(payload)

    @router.delete("/{item_id}", response_model=SharedRecipeCollectionMemberOut)
    def delete_one(self, collection_id: UUID4, item_id: UUID4):
        member = self.repo.get_one(item_id)
        if not member or member.collection_id != collection_id:
            raise HTTPException(status.HTTP_404_NOT_FOUND, ErrorResponse.respond(message="Not found."))
        return self.mixins.delete_one(item_id)
