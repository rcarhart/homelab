from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, orm
from sqlalchemy.orm import Mapped, mapped_column

from mealie.db.models._model_base import BaseMixins, SqlAlchemyBase
from mealie.db.models._model_utils.auto_init import auto_init
from mealie.db.models._model_utils.guid import GUID

if TYPE_CHECKING:
    from mealie.db.models.recipe.recipe import RecipeModel
    from mealie.db.models.users.users import User
    from .shared_recipe_collection import SharedRecipeCollection


class SharedRecipeLink(SqlAlchemyBase, BaseMixins):
    __tablename__ = "shared_recipe_links"
    __table_args__: tuple[UniqueConstraint, ...] = (
        UniqueConstraint("collection_id", "recipe_id", name="shared_recipe_link_unique_key"),
    )

    id: Mapped[GUID] = mapped_column(GUID, primary_key=True, default=GUID.generate)

    collection_id: Mapped[GUID] = mapped_column(
        GUID, ForeignKey("shared_recipe_collections.id"), nullable=False, index=True
    )
    collection: Mapped["SharedRecipeCollection"] = orm.relationship("SharedRecipeCollection", back_populates="recipe_links")

    recipe_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("recipes.id"), nullable=False, index=True)
    recipe: Mapped["RecipeModel"] = orm.relationship("RecipeModel", foreign_keys=[recipe_id])

    shared_by_user_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("users.id"), nullable=False, index=True)
    shared_by_user: Mapped["User"] = orm.relationship("User", foreign_keys=[shared_by_user_id])

    @auto_init()
    def __init__(self, **_) -> None:
        pass

    def update(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
