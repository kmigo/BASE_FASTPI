"""uuid

Revision ID: 3ab36326c016
Revises: 7a6bfb6bac5b
Create Date: 2023-04-15 15:37:33.692162

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3ab36326c016'
down_revision = '7a6bfb6bac5b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('DROP TABLE IF EXISTS events CASCADE')
    op.execute('DROP TABLE IF EXISTS users CASCADE')
    op.execute('DROP TABLE IF EXISTS employees_events CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
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
    sa.Column('producer_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('ACTIVATE', 'INACTIVATE', 'PENDING', name='employeesstatus'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='employees_events_event_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['producer_id'], ['users.id'], name='employees_events_producer_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='employees_events_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='employees_events_pkey')
    )
    op.create_table('events',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='events_pkey')
    )
    # ### end Alembic commands ###
