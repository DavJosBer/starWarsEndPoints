"""empty message

Revision ID: 429ac97dddf9
Revises: 1694502753ef
Create Date: 2021-03-31 15:39:34.380016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '429ac97dddf9'
down_revision = '1694502753ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'user', ['name'])
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###