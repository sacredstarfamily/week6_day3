"""add task

Revision ID: 036cd9118090
Revises: 44c91bf6542e
Create Date: 2024-03-27 08:06:35.449266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '036cd9118090'
down_revision = '44c91bf6542e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
