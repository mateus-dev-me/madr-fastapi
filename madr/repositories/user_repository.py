from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.database.models import User


def get_user_by_username_or_email(
    session: Session, username: str, email: str
) -> User | None:
    return session.scalar(
        select(User).where((User.username == username) | (User.email == email))
    )


def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def list_users(session: Session) -> Sequence[User]:
    return session.scalars(select(User)).all()


def update_user(session: Session, user: User) -> User:
    session.commit()
    session.refresh(user)
    return user


def delete_user(session, user: User) -> None:
    session.delete(user)
    session.commit()
