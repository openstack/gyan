"""Add flavor table

Revision ID: 395aff469925
Revises: f3bf9414f399
Create Date: 2018-10-22 07:53:38.240884

"""

# revision identifiers, used by Alembic.
revision = '395aff469925'
down_revision = 'f3bf9414f399'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flavor',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('python_version', sa.String(length=255), nullable=False),
    sa.Column('cpu', sa.String(length=255), nullable=False),
    sa.Column('driver', sa.String(length=255), nullable=False),
    sa.Column('memory', sa.String(length=255), nullable=False),
    sa.Column('disk', sa.String(length=255), nullable=False),
    sa.Column('additional_details', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
