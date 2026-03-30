"""add shared recipe collections

Revision ID: b1f4c7d9e2aa
Revises: cdc93edaf73d
Create Date: 2026-03-30 19:35:00.000000

"""

import sqlalchemy as sa
from alembic import op

from mealie.db.migration_types import GUID

# revision identifiers, used by Alembic.
revision = "b1f4c7d9e2aa"
down_revision: str | None = "cdc93edaf73d"
branch_labels: str | tuple[str, ...] | None = None
depends_on: str | tuple[str, ...] | None = None


def upgrade():
    with op.batch_alter_table("recipes", schema=None) as batch_op:
        batch_op.add_column(sa.Column("source_recipe_id", GUID(), nullable=True))
        batch_op.add_column(
            sa.Column(
                "is_household_copy",
                sa.Boolean(),
                nullable=False,
                default=False,
                server_default=sa.sql.expression.false(),
            )
        )
        batch_op.create_index("ix_recipes_source_recipe_id", ["source_recipe_id"], unique=False)
        batch_op.create_foreign_key("fk_recipes_source_recipe_id", "recipes", ["source_recipe_id"], ["id"])

    op.create_table(
        "shared_recipe_collections",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("visibility_mode", sa.String(), nullable=False),
        sa.Column(
            "allow_comments",
            sa.Boolean(),
            nullable=False,
            default=True,
            server_default=sa.sql.expression.true(),
        ),
        sa.Column(
            "allow_copy",
            sa.Boolean(),
            nullable=False,
            default=True,
            server_default=sa.sql.expression.true(),
        ),
        sa.Column("owner_user_id", GUID(), nullable=False),
        sa.Column("origin_group_id", GUID(), nullable=False),
        sa.Column("origin_household_id", GUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("last_modified", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["origin_group_id"], ["groups.id"]),
        sa.ForeignKeyConstraint(["origin_household_id"], ["households.id"]),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug", name="shared_recipe_collection_slug_key"),
    )
    op.create_index(
        "ix_shared_recipe_collections_slug", "shared_recipe_collections", ["slug"], unique=False
    )
    op.create_index(
        "ix_shared_recipe_collections_owner_user_id",
        "shared_recipe_collections",
        ["owner_user_id"],
        unique=False,
    )
    op.create_index(
        "ix_shared_recipe_collections_origin_group_id",
        "shared_recipe_collections",
        ["origin_group_id"],
        unique=False,
    )
    op.create_index(
        "ix_shared_recipe_collections_origin_household_id",
        "shared_recipe_collections",
        ["origin_household_id"],
        unique=False,
    )

    op.create_table(
        "shared_recipe_collection_members",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.Column(
            "can_comment",
            sa.Boolean(),
            nullable=False,
            default=True,
            server_default=sa.sql.expression.true(),
        ),
        sa.Column(
            "can_copy",
            sa.Boolean(),
            nullable=False,
            default=True,
            server_default=sa.sql.expression.true(),
        ),
        sa.Column("collection_id", GUID(), nullable=False),
        sa.Column("user_id", GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("last_modified", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["collection_id"], ["shared_recipe_collections.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("collection_id", "user_id", name="shared_recipe_collection_member_unique_key"),
    )
    op.create_index(
        "ix_shared_recipe_collection_members_collection_id",
        "shared_recipe_collection_members",
        ["collection_id"],
        unique=False,
    )
    op.create_index(
        "ix_shared_recipe_collection_members_user_id",
        "shared_recipe_collection_members",
        ["user_id"],
        unique=False,
    )

    op.create_table(
        "shared_recipe_links",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("collection_id", GUID(), nullable=False),
        sa.Column("recipe_id", GUID(), nullable=False),
        sa.Column("shared_by_user_id", GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("last_modified", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["collection_id"], ["shared_recipe_collections.id"]),
        sa.ForeignKeyConstraint(["recipe_id"], ["recipes.id"]),
        sa.ForeignKeyConstraint(["shared_by_user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("collection_id", "recipe_id", name="shared_recipe_link_unique_key"),
    )
    op.create_index("ix_shared_recipe_links_collection_id", "shared_recipe_links", ["collection_id"], unique=False)
    op.create_index("ix_shared_recipe_links_recipe_id", "shared_recipe_links", ["recipe_id"], unique=False)
    op.create_index(
        "ix_shared_recipe_links_shared_by_user_id", "shared_recipe_links", ["shared_by_user_id"], unique=False
    )

    op.create_table(
        "shared_recipe_comments",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("text", sa.String(), nullable=True),
        sa.Column("collection_id", GUID(), nullable=False),
        sa.Column("recipe_id", GUID(), nullable=False),
        sa.Column("user_id", GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("last_modified", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["collection_id"], ["shared_recipe_collections.id"]),
        sa.ForeignKeyConstraint(["recipe_id"], ["recipes.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_shared_recipe_comments_collection_id", "shared_recipe_comments", ["collection_id"], unique=False
    )
    op.create_index("ix_shared_recipe_comments_recipe_id", "shared_recipe_comments", ["recipe_id"], unique=False)
    op.create_index("ix_shared_recipe_comments_user_id", "shared_recipe_comments", ["user_id"], unique=False)


def downgrade():
    op.drop_index("ix_shared_recipe_comments_user_id", table_name="shared_recipe_comments")
    op.drop_index("ix_shared_recipe_comments_recipe_id", table_name="shared_recipe_comments")
    op.drop_index("ix_shared_recipe_comments_collection_id", table_name="shared_recipe_comments")
    op.drop_table("shared_recipe_comments")

    op.drop_index("ix_shared_recipe_links_shared_by_user_id", table_name="shared_recipe_links")
    op.drop_index("ix_shared_recipe_links_recipe_id", table_name="shared_recipe_links")
    op.drop_index("ix_shared_recipe_links_collection_id", table_name="shared_recipe_links")
    op.drop_table("shared_recipe_links")

    op.drop_index("ix_shared_recipe_collection_members_user_id", table_name="shared_recipe_collection_members")
    op.drop_index(
        "ix_shared_recipe_collection_members_collection_id", table_name="shared_recipe_collection_members"
    )
    op.drop_table("shared_recipe_collection_members")

    op.drop_index("ix_shared_recipe_collections_origin_household_id", table_name="shared_recipe_collections")
    op.drop_index("ix_shared_recipe_collections_origin_group_id", table_name="shared_recipe_collections")
    op.drop_index("ix_shared_recipe_collections_owner_user_id", table_name="shared_recipe_collections")
    op.drop_index("ix_shared_recipe_collections_slug", table_name="shared_recipe_collections")
    op.drop_table("shared_recipe_collections")

    with op.batch_alter_table("recipes", schema=None) as batch_op:
        batch_op.drop_constraint("fk_recipes_source_recipe_id", type_="foreignkey")
        batch_op.drop_index("ix_recipes_source_recipe_id")
        batch_op.drop_column("is_household_copy")
        batch_op.drop_column("source_recipe_id")
