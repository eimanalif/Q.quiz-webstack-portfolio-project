"""empty message

Revision ID: d67c48fed2df
Revises: 117c8db38858
Create Date: 2024-09-17 16:49:43.524739+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67c48fed2df'
down_revision = '117c8db38858'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('option',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('text', sa.String(length=255), nullable=False),
    # sa.Column('question_id', sa.Integer(), nullable=False),
    # sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('option_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_result_option', 'option', ['option_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('option_id')

    op.drop_table('option')
    # ### end Alembic commands ###
