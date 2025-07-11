"""add creator_id with FK name

Revision ID: 66cd29961ad2
Revises: 8d34a847db61
Create Date: 2025-06-02 19:47:33.797937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66cd29961ad2'
down_revision = '8d34a847db61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.drop_column('location')

    # ### end Alembic commands ###
