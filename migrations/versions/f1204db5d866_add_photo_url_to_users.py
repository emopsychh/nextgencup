"""add photo_url to users

Revision ID: f1204db5d866
Revises: 62fbc0136296
Create Date: 2025-05-03 17:14:02.183878
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f1204db5d866'
down_revision = '62fbc0136296'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    # добавляем колонку photo_url в users
    op.add_column(
        'users',
        sa.Column('photo_url', sa.String(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # откатываем добавление колонки
    op.drop_column('users', 'photo_url')
