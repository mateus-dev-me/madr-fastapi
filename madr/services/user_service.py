from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from madr.models import User
from madr.repositories import user_repository


def create_user(session: Session, user: User) -> User:
    exist_user = user_repository.get_user_by_username_or_email(
        session, user.username, user.email
    )
    if exist_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Username or e-mail already exists',
        )

    user = user_repository.create_user(session, user)
    return user


def list_users(session: Session):
    users = user_repository.list_users(session)
    return users


def detail_user(session: Session, user: User) -> User:
    user = user_repository.get_user_by_id(session, user.id)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    return user


def update_user(session: Session, user: User) -> User:
    user = user_repository.get_user_by_id(session, user.id)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    updated_user = user_repository.update_user(session, user)
    return updated_user


def delete_user(session: Session, user: User):
    user = user_repository.get_user_by_id(session, user.id)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_repository.delete_user(session, user)
