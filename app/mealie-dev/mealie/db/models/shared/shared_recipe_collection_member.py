from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint, orm
from sqlalchemy.orm import Mapped, mapped_column

from mealie.db.models._model_base import BaseMixins, SqlAlchemyBase
from mealie.db.models._model_utils.auto_init import auto_init
from mealie.db.models._model_utils.guid import GUID

if TYPE_CHECKING:
    from mealie.db.models.users.users import User
    from .shared_recipe_collection import SharedRecipeCollection


class SharedRecipeCollectionMember(SqlAlchemyBase, BaseMixins):
    __tablename__ = "shared_recipe_collection_members"
    __table_args__: tuple[UniqueConstraint, ...] = (
        UniqueConstraint("collection_id", "user_id", name="shared_recipe_collection_member_unique_key"),
    )

    id: Mapped[GUID] = mapped_column(GUID, primary_key=True, default=GUID.generate)
    role: Mapped[str] = mapped_column(String, nullable=False, default="member")
    can_comment: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    can_copy: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    collection_id: Mapped[GUID] = mapped_column(
        GUID, ForeignKey("shared_recipe_collections.id"), nullable=False, index=True
    )
    collection: Mapped["SharedRecipeCollection"] = orm.relationship("SharedRecipeCollection", back_populates="members")

    user_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("users.id"), nullable=False, index=True)
    user: Mapped["User"] = orm.relationship("User", foreign_keys=[user_id])

    @auto_init()
    def __init__(self, **_) -> None:
        pass

    def update(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
