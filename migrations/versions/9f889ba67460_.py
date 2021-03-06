"""empty message

Revision ID: 9f889ba67460
Revises: 
Create Date: 2021-02-11 15:52:27.345337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f889ba67460'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classdrugs')
    op.drop_table('years')
    op.drop_table('drugs')
    op.drop_table('drug_class')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('hash_password', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('username', name='users_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('drug_class',
    sa.Column('id_drug', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_class', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_class'], ['classdrugs.id'], name='drug_class_id_class_fkey'),
    sa.ForeignKeyConstraint(['id_drug'], ['drugs.id'], name='drug_class_id_drug_fkey')
    )
    op.create_table('drugs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('colloquial_name', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('sicenc_name', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('opening_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('formula', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('discoverer', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('user', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['opening_year'], ['years.year'], name='drugs_opening_year_fkey'),
    sa.ForeignKeyConstraint(['user'], ['users.username'], name='drugs_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='drugs_pkey'),
    sa.UniqueConstraint('formula', name='drugs_formula_key')
    )
    op.create_table('years',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='years_pkey'),
    sa.UniqueConstraint('year', name='years_year_key')
    )
    op.create_table('classdrugs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('drugs_class', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='classdrugs_pkey'),
    sa.UniqueConstraint('drugs_class', name='classdrugs_drugs_class_key')
    )
    # ### end Alembic commands ###
