"""create users table v2

Revision ID: 300bc24efed6
Revises: 67661f333b8f
Create Date: 2022-12-11 11:07:45.824041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '300bc24efed6'
down_revision = '67661f333b8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('base', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(length=32), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('base', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')
        batch_op.drop_column('username')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
