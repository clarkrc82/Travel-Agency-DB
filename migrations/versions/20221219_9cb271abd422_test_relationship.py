"""test relationship

Revision ID: 9cb271abd422
Revises: d363748b0016
Create Date: 2022-12-19 09:05:26.559385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb271abd422'
down_revision = 'd363748b0016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_trips')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_trips',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('trip_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], name='user_trips_trip_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_trips_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', 'user_id', 'trip_id', name='user_trips_pkey')
    )
    # ### end Alembic commands ###
