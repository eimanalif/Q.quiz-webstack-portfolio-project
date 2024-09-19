"""empty message

Revision ID: f444fc7046f4
Revises: d67c48fed2df
Create Date: 2024-09-18 18:48:43.682809+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f444fc7046f4'
down_revision = 'd67c48fed2df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
#     op.create_table('choice',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('text', sa.String(length=255), nullable=False),
#     sa.Column('question_id', sa.Integer(), nullable=True),
#     sa.Column('is_correct', sa.Boolean(), nullable=True),
#     sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
#     sa.PrimaryKeyConstraint('id')
#     )
    op.drop_table('Choice')
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_text', sa.String(length=500), nullable=False))
        batch_op.drop_column('text')

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(length=500), nullable=False))
        batch_op.alter_column('quiz_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('question_text')

    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('score', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('score', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_text', sa.VARCHAR(length=500), nullable=False))
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('quiz_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('content')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.VARCHAR(length=500), nullable=False))
        batch_op.drop_column('question_text')

    op.create_table('Choice',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('choice')
    # ### end Alembic commands ###
