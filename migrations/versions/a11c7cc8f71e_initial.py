"""initial

Revision ID: a11c7cc8f71e
Revises: 3d5c95a58619
Create Date: 2016-10-31 15:51:35.220000

"""

# revision identifiers, used by Alembic.
revision = 'a11c7cc8f71e'
down_revision = '3d5c95a58619'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###