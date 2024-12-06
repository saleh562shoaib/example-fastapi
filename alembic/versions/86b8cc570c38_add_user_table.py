"""add user table

Revision ID: 86b8cc570c38
Revises: dab32edb03eb
Create Date: 2024-12-02 00:58:32.572873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86b8cc570c38'
down_revision: Union[str, None] = 'dab32edb03eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                        sa.Column('id', sa.Integer(), nullable=False),
                        sa.Column('email', sa.String(), nullable=False),
                        sa.Column('password', sa.String(), nullable=False),
                        sa.Column('created_at', sa.TIMESTAMP(timezone=False),
                                  server_default=sa.text('now()'), nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                        sa.UniqueConstraint('email')                           
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
