"""Create User, Romatist and Book Tables

Revision ID: 3dd9d46b982a
Revises: 
Create Date: 2025-03-01 18:33:46.305341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dd9d46b982a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('novelists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('death_date', sa.Date(), nullable=True),
    sa.Column('nationality', sa.String(length=100), nullable=True),
    sa.Column('awards', sa.Text(), nullable=True),
    sa.Column('social_media_links', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('profile_picture', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=17), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.Column('subgenre', sa.String(length=100), nullable=True),
    sa.Column('tropes', sa.Text(), nullable=True),
    sa.Column('heat_level', sa.Integer(), nullable=True),
    sa.Column('target_audience', sa.String(length=50), nullable=True),
    sa.Column('publisher', sa.String(length=100), nullable=True),
    sa.Column('edition', sa.Integer(), nullable=True),
    sa.Column('published_date', sa.Date(), nullable=True),
    sa.Column('novelist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['novelist_id'], ['novelists.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn'),
    sa.UniqueConstraint('title')
    )
    op.create_table('user_favorite_books',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'book_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorite_books')
    op.drop_table('books')
    op.drop_table('users')
    op.drop_table('novelists')
    # ### end Alembic commands ###
