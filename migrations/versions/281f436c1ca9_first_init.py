"""first init

Revision ID: 281f436c1ca9
Revises: 
Create Date: 2023-09-19 22:24:23.021579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281f436c1ca9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('me',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=6), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('links', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('me')
    # ### end Alembic commands ###
