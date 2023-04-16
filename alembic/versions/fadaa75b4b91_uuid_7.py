"""uuid 7

Revision ID: fadaa75b4b91
Revises: 20e74aef4b7c
Create Date: 2023-04-15 19:25:52.173212

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fadaa75b4b91'
down_revision = '20e74aef4b7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_events')
    op.drop_table('users')
    op.drop_table('events')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('producer_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='events_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('employees_events',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('event_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('ACTIVATE', 'INACTIVATE', 'PENDING', name='employeesstatus'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='employees_events_event_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='employees_events_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='employees_events_pkey')
    )
    # ### end Alembic commands ###
