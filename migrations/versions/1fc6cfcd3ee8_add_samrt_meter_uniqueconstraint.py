"""add samrt_meter UniqueConstraint

Revision ID: 1fc6cfcd3ee8
Revises: 8588f799a59b
Create Date: 2021-05-17 22:36:38.352968

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1fc6cfcd3ee8'
down_revision = '8588f799a59b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('smart_meters', 'uuid',
               existing_type=mysql.VARCHAR(length=36),
               nullable=True)
    op.create_unique_constraint('unique_smart_meter', 'smart_meters', ['meter_name', 'home_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_smart_meter', 'smart_meters', type_='unique')
    op.alter_column('smart_meters', 'uuid',
               existing_type=mysql.VARCHAR(length=36),
               nullable=False)
    # ### end Alembic commands ###