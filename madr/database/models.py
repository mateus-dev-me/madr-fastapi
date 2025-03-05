from datetime import date, datetime

from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship
from sqlalchemy.sql import func

table_registry = registry()

user_favorite_books = Table(
    'user_favorite_books',
    table_registry.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True),
)


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    profile_picture: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    favorite_books: Mapped[list['Book']] = relationship(
        init=False,
        secondary=user_favorite_books,
        back_populates='favorited_by',
    )


@table_registry.mapped_as_dataclass
class Novelist:
    __tablename__ = 'novelists'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    biography: Mapped[str] = mapped_column(Text, nullable=True)
    birth_date: Mapped[date] = mapped_column(nullable=True)
    death_date: Mapped[date] = mapped_column(nullable=True)
    nationality: Mapped[str] = mapped_column(String(100), nullable=True)
    awards: Mapped[str] = mapped_column(Text, nullable=True)
    social_media_links: Mapped[dict] = mapped_column(JSON, nullable=True)

    books: Mapped[list['Book']] = relationship(
        init=False, back_populates='novelist', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Book:
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(String(17), unique=True, nullable=True)
    pages: Mapped[int] = mapped_column(Integer, nullable=True)
    genre: Mapped[str] = mapped_column(String(100), nullable=True)
    subgenre: Mapped[str] = mapped_column(
        String(100), nullable=True
    )  # Romance histórico, fantasia romântica, etc.
    tropes: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Ex: "inimigos para amantes, amor proibido"
    heat_level: Mapped[int] = mapped_column(
        Integer, nullable=True
    )  # Escala de 1 a 5
    target_audience: Mapped[str] = mapped_column(
        String(50), nullable=True
    )  # Ex: "adulto", "jovem adulto"
    publisher: Mapped[str] = mapped_column(String(100), nullable=True)
    edition: Mapped[int] = mapped_column(Integer, nullable=True)
    published_date: Mapped[date] = mapped_column(nullable=True)

    novelist_id: Mapped[int] = mapped_column(
        ForeignKey('novelists.id'),
        nullable=False,
    )
    novelist: Mapped['Novelist'] = relationship(
        init=False, back_populates='books'
    )
    favorited_by: Mapped['User'] = relationship(
        init=False,
        secondary=user_favorite_books,
        back_populates='favorite_books',
    )
