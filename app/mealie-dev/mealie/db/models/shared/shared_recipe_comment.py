from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, orm
from sqlalchemy.orm import Mapped, mapped_column

from mealie.db.models._model_base import BaseMixins, SqlAlchemyBase
from mealie.db.models._model_utils.auto_init import auto_init
from mealie.db.models._model_utils.guid import GUID

if TYPE_CHECKING:
    from mealie.db.models.recipe.recipe import RecipeModel
    from mealie.db.models.users.users import User
    from .shared_recipe_collection import SharedRecipeCollection


class SharedRecipeComment(SqlAlchemyBase, BaseMixins):
    __tablename__ = "shared_recipe_comments"

    id: Mapped[GUID] = mapped_column(GUID, primary_key=True, default=GUID.generate)
    text: Mapped[str | None] = mapped_column(String)

    collection_id: Mapped[GUID] = mapped_column(
        GUID, ForeignKey("shared_recipe_collections.id"), nullable=False, index=True
    )
    collection: Mapped["SharedRecipeCollection"] = orm.relationship("SharedRecipeCollection", back_populates="comments")

    recipe_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("recipes.id"), nullable=False, index=True)
    recipe: Mapped["RecipeModel"] = orm.relationship("RecipeModel", foreign_keys=[recipe_id])

    user_id: Mapped[GUID] = mapped_column(GUID, ForeignKey("users.id"), nullable=False, index=True)
    user: Mapped["User"] = orm.relationship("User", foreign_keys=[user_id])

    @auto_init()
    def __init__(self, **_) -> None:
        pass

    def update(self, text, **_) -> None:
        self.text = text
