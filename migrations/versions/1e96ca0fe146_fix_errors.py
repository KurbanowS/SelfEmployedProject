"""fix errors

Revision ID: 1e96ca0fe146
Revises: 
Create Date: 2023-09-23 20:59:59.953631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e96ca0fe146'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('designers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'name', 'email')
    )
    op.create_table('developers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.drop_table('developers')
    op.drop_table('designers')
    # ### end Alembic commands ###