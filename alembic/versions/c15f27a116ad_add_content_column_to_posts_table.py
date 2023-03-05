"""add content column to posts table

Revision ID: c15f27a116ad
Revises: 0492da384d1d
Create Date: 2023-02-28 15:21:26.668577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c15f27a116ad'
down_revision = '0492da384d1d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(('content'), sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
