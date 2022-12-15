"""user_trips FK

Revision ID: 132d6608546d
Revises: 2f6dfe0a606a
Create Date: 2022-12-14 23:09:59.662220

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '132d6608546d'
down_revision = '2f6dfe0a606a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_trips',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id', 'trip_id')
    )
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)

    op.drop_table('user_trips')
    # ### end Alembic commands ###