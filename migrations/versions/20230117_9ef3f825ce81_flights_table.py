"""flights table

Revision ID: 9ef3f825ce81
Revises: 991bfa14347c
Create Date: 2023-01-17 19:39:40.788041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ef3f825ce81'
down_revision = '991bfa14347c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('flight_num', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('orgin_id', sa.Integer(), nullable=False),
    sa.Column('destination_id', sa.Integer(), nullable=False),
    sa.Column('airline_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['airline_id'], ['airlines.id'], ),
    sa.ForeignKeyConstraint(['destination_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['orgin_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('flight_num')
    )
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'flights', ['flight_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('flights')
    # ### end Alembic commands ###
