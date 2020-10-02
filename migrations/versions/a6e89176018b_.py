"""empty message

Revision ID: a6e89176018b
Revises: d21810f719b6
Create Date: 2020-10-01 10:44:18.714320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6e89176018b'
down_revision = 'd21810f719b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_name', sa.String(length=120), nullable=False))
    op.add_column('Show', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('Show', sa.Column('name', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'name')
    op.drop_column('Show', 'image_link')
    op.drop_column('Show', 'artist_name')
    # ### end Alembic commands ###
