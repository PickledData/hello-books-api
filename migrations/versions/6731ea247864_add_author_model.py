"""add author model

Revision ID: 6731ea247864
Revises: 5185f07bff38
Create Date: 2024-11-05 09:45:54.083610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6731ea247864'
down_revision = '5185f07bff38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'author', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('author_id')

    op.drop_table('author')
    # ### end Alembic commands ###