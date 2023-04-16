"""uuid 4

Revision ID: 72c18d845383
Revises: f94c8e5738f9
Create Date: 2023-04-15 18:30:07.458207

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '72c18d845383'
down_revision = 'f94c8e5738f9'
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
    op.create_table('employees_events',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('event_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('ACTIVATE', 'INACTIVATE', 'PENDING', name='employeesstatus'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='employees_events_event_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='employees_events_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='employees_events_pkey')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    op.create_table('events',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='events_pkey')
    )
    # ### end Alembic commands ###
