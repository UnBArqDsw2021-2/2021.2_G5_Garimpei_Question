"""init

Revision ID: 949cab9c6e12
Revises: 
Create Date: 2022-03-08 19:32:05.637456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '949cab9c6e12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('example')
    # ### end Alembic commands ###