"""add expected_end to loans

Revision ID: 20250217180000
Revises: ee9d5d295b3c
Create Date: 2024-02-17 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20250217180000'
down_revision = 'ee9d5d295b3c'
branch_labels = None
depends_on = None


def upgrade():
    # Adiciona a coluna expected_end na tabela loans
    op.add_column('loans', sa.Column('expected_end', sa.DateTime(), nullable=True))


def downgrade():
    # Remove a coluna expected_end da tabela loans
    op.drop_column('loans', 'expected_end') 