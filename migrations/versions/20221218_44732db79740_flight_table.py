"""Flight table

Revision ID: 44732db79740
Revises: 8db984d8a779
Create Date: 2022-12-18 21:11:47.613995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44732db79740'
down_revision = '8db984d8a779'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('flight_num', sa.Integer(), nullable=False),
    sa.Column('orgin_id', sa.Integer(), nullable=False),
    sa.Column('destination_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('airline_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('flight_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flights')
    # ### end Alembic commands ###
