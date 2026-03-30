from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint, orm
from sqlalchemy.orm import Mapped, mapped_column

from mealie.db.models._model_base import BaseMixins, SqlAlchemyBase
from mealie.db.models._model_utils.auto_init import auto_init
from mealie.db.models._model_utils.guid import GUID

if TYPE_CHECKING:
    from mealie.db.models.group.group import Group
    from mealie.db.models.household.household import Household
    from mealie.db.models.users.users import User
    from .shared_recipe_collection_member import SharedRecipeCollectionMember
    from .shared_recipe_comment import SharedRecipeComment
    from .shared_recipe_link import SharedRecipeLink


class SharedRecipeCollection(SqlAlchemyBase, BaseMixins):
    __tablename__ = "shared_recipe_collections"
    __table_args__: tuple[UniqueConstraint, ...] = (
        UniqueConstraint("slug", name="shared_recipe_collection_slug_key"),
    )

    id: Mapped[GUID] = mapped_column(GUID, primary_key=True, default=GUID.generate)
    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String, default="")
    visibility_mode: Mapped[str] = mapped_column(String, nullable=False, default="private_membership")
    allow_comments: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    allow_copy: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    owner_user_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("users.id"), nullable=False, index=True)
    owner: Mapped["User"] = orm.relationship("User", foreign_keys=[owner_user_id])

    origin_group_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("groups.id"), nullable=False, index=True)
    origin_group: Mapped["Group"] = orm.relationship("Group", foreign_keys=[origin_group_id])

    origin_household_id: Mapped[GUID | None] = mapped_column(GUID, ForeignKey("households.id"), index=True)
    origin_household: Mapped["Household | None"] = orm.relationship("Household", foreign_keys=[origin_household_id])

    members: Mapped[list["SharedRecipeCollectionMember"]] = orm.relationship(
        "SharedRecipeCollectionMember", back_populates="collection", cascade="all, delete-orphan"
    )
    recipe_links: Mapped[list["SharedRecipeLink"]] = orm.relationship(
        "SharedRecipeLink", back_populates="collection", cascade="all, delete-orphan"
    )
    comments: Mapped[list["SharedRecipeComment"]] = orm.relationship(
        "SharedRecipeComment", back_populates="collection", cascade="all, delete-orphan"
    )

    @auto_init()
    def __init__(self, **_) -> None:
        pass

    def update(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
