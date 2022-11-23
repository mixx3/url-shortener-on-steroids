"""auth

Revision ID: eda01c95d8d2
Revises: 2c206b6f5d0d
Create Date: 2022-11-24 01:38:39.744013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eda01c95d8d2'
down_revision = '2c206b6f5d0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('salt', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.add_column('url', sa.Column('user_id', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'url', ['id'])
    op.create_foreign_key(None, 'url', 'auth', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'url', type_='foreignkey')
    op.drop_constraint(None, 'url', type_='unique')
    op.drop_column('url', 'user_id')
    op.drop_table('auth')
    # ### end Alembic commands ###
