"""empty message

Revision ID: e870cb2c9c06
Revises: 7188f06c04e5
Create Date: 2023-09-19 16:49:37.358798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e870cb2c9c06'
down_revision = '7188f06c04e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.alter_column('yearCompleted',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_column('gender')
        batch_op.drop_column('health')
        batch_op.drop_column('kin')
        batch_op.drop_column('admitted')
        batch_op.drop_column('marital')
        batch_op.drop_column('school')
        batch_op.drop_column('hallofresidence')
        batch_op.drop_column('department')
        batch_op.drop_column('guardian')
        batch_op.drop_column('faculty')
        batch_op.drop_column('work')
        batch_op.drop_column('relationship')
        batch_op.drop_column('address')
        batch_op.drop_column('program')
        batch_op.drop_column('nationality')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nationality', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('program', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('relationship', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('work', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('faculty', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('guardian', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('hallofresidence', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('school', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('marital', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('admitted', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('kin', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('health', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.alter_column('yearCompleted',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###
