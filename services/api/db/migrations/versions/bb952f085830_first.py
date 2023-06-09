"""first

Revision ID: bb952f085830
Revises: 
Create Date: 2023-03-13 00:46:25.760523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb952f085830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_table',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('balance', sa.FLOAT(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions_table',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('transaction_type', sa.String(), nullable=False),
    sa.Column('amount', sa.FLOAT(), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'id'),
    sa.UniqueConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions_table')
    op.drop_table('users_table')
    # ### end Alembic commands ###
