"""Create task table

Revision ID: 4756ed42f5bd
Revises: 
Create Date: 2024-03-06 16:03:47.351487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4756ed42f5bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('completion_status', sa.Boolean,
                  nullable=False, default=False)
    )


def downgrade() -> None:
    op.drop_table('tasks')
