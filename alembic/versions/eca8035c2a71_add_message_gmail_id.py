"""add message gmail id

Revision ID: eca8035c2a71
Revises: e836155c0355
Create Date: 2026-09-16 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'eca8035c2a71'
down_revision: Union[str, Sequence[str], None] = 'e836155c0355'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('messages', sa.Column('gmail_message_id', sa.Text(), nullable=True))
    op.create_unique_constraint('uq_messages_gmail_message_id', 'messages', ['gmail_message_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('uq_messages_gmail_message_id', 'messages', type_='unique')
    op.drop_column('messages', 'gmail_message_id')
