"""Create role model

Revision ID: e24ce3e75fac
Revises: 1cd82b90c788
Create Date: 2023-12-08 22:47:38.301716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e24ce3e75fac'
down_revision = '1cd82b90c788'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    # ### end Alembic commands ###
