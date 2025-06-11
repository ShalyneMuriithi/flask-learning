"""Add phone to the database

Revision ID: fa6735a4bc95
Revises: 1f7cabaddfec
Create Date: 2025-06-10 16:17:57.802480

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa6735a4bc95'
down_revision = '1f7cabaddfec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Students', sa.Column('phone', sa.String(20), nullable=True))

def downgrade():
    op.drop_column('Students', 'phone')
