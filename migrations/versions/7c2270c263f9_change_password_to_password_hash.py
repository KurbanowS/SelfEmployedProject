"""Change password to password_hash

Revision ID: 7c2270c263f9
Revises: 4e5fbf97501b
Create Date: 2023-10-01 16:13:54.444905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2270c263f9'
down_revision = '4e5fbf97501b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('me', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=40), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('me', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=40), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###