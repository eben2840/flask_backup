"""empty message

Revision ID: b8171d3e1054
Revises: 9125e4a6f8a5
Create Date: 2023-10-14 18:46:07.688612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8171d3e1054'
down_revision = '9125e4a6f8a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pdf_file', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_column('pdf_file')

    # ### end Alembic commands ###
