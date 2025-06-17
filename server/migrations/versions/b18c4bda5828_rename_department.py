"""rename department

Revision ID: b18c4bda5828
Revises: a2b2dd14b79d
Create Date: 2025-06-17 23:35:11.477715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18c4bda5828'
down_revision = 'a2b2dd14b79d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address', new_column_name='location')
def downgrade():
    op.alter_column('departments', 'location', new_column_name='address')
