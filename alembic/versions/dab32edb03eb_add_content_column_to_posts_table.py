"""add content column to posts table

Revision ID: dab32edb03eb
Revises: 8cb09dfa2f01
Create Date: 2024-12-01 01:29:35.012131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dab32edb03eb'
down_revision: Union[str, None] = '8cb09dfa2f01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# alembic --help معه ستعرف كل شئ عنه
# alembic revision -m "add اسم الجدول" 

def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
