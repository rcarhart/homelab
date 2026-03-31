from datetime import datetime

from pydantic import UUID4, ConfigDict
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.interfaces import LoaderOption

from mealie.db.models.shared.shared_recipe_collection import SharedRecipeCollection
from mealie.db.models.shared.shared_recipe_collection_member import SharedRecipeCollectionMember
from mealie.db.models.shared.shared_recipe_comment import SharedRecipeComment
from mealie.db.models.shared.shared_recipe_link import SharedRecipeLink
from mealie.db.models.users.users import User
from mealie.schema._mealie import MealieModel
from mealie.schema._mealie.mealie_model import UpdatedAtField
from mealie.schema.recipe.recipe import RecipeSummary
from mealie.schema.response.pagination import PaginationBase


class SharedCollectionUserBase(MealieModel):
    id: UUID4
    username: str | None = None
    full_name: str | None = None
    model_config = ConfigDict(from_attributes=True)


class SharedRecipeCollectionCreate(MealieModel):
    name: str
    description: str = ""
    slug: str | None = None
    visibility_mode: str = "private_membership"
    allow_comments: bool = True
    allow_copy: bool = True


class SharedRecipeCollectionSave(SharedRecipeCollectionCreate):
    owner_user_id: UUID4
    origin_group_id: UUID4
    origin_household_id: UUID4 | None = None


class SharedRecipeCollectionUpdate(SharedRecipeCollectionSave):
    id: UUID4


class SharedRecipeCollectionOut(SharedRecipeCollectionUpdate):
    owner: SharedCollectionUserBase | None = None
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def loader_options(cls) -> list[LoaderOption]:
        return [joinedload(SharedRecipeCollection.owner)]


class SharedRecipeCollectionMemberCreate(MealieModel):
    collection_id: UUID4
    user_id: UUID4
    role: str = "member"
    can_comment: bool = True
    can_copy: bool = True


class SharedRecipeCollectionMemberOut(SharedRecipeCollectionMemberCreate):
    id: UUID4
    created_at: datetime
    updated_at: datetime = UpdatedAtField(...)
    user: SharedCollectionUserBase | None = None
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def loader_options(cls) -> list[LoaderOption]:
        return [joinedload(SharedRecipeCollectionMember.user)]


class SharedRecipeLinkCreate(MealieModel):
    collection_id: UUID4
    recipe_id: UUID4
    shared_by_user_id: UUID4 | None = None


class SharedRecipeLinkOut(SharedRecipeLinkCreate):
    id: UUID4
    created_at: datetime
    updated_at: datetime = UpdatedAtField(...)
    recipe: RecipeSummary | None = None
    shared_by_user: SharedCollectionUserBase | None = None
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def loader_options(cls) -> list[LoaderOption]:
        return [joinedload(SharedRecipeLink.shared_by_user), joinedload(SharedRecipeLink.recipe)]


class SharedRecipeCommentCreate(MealieModel):
    collection_id: UUID4
    recipe_id: UUID4
    user_id: UUID4 | None = None
    text: str


class SharedRecipeCommentOut(SharedRecipeCommentCreate):
    id: UUID4
    created_at: datetime
    updated_at: datetime = UpdatedAtField(...)
    user: SharedCollectionUserBase | None = None
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def loader_options(cls) -> list[LoaderOption]:
        return [joinedload(SharedRecipeComment.user)]


class SharedRecipeCopyRequest(MealieModel):
    name: str | None = None


class SharedRecipeCollectionPagination(PaginationBase):
    items: list[SharedRecipeCollectionOut]
