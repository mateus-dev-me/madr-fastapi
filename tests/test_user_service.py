from http import HTTPStatus

import pytest
from fastapi.exceptions import HTTPException

from madr.services import user_service
from tests.factories import UserFactory


def test_create_user_service(session):
    user_data = UserFactory.build()
    created_user = user_service.create_user(session, user_data)
    assert created_user == user_data


def test_create_user_with_exist_username_service(session, user):
    new_user = UserFactory.build()
    new_user.username = user.username

    with pytest.raises(HTTPException) as exc_info:
        user_service.create_user(session, new_user)

    assert exc_info.value.status_code == HTTPStatus.BAD_REQUEST
    assert exc_info.value.detail == 'Username or e-mail already exists'


def test_create_user_with_exist_email_service(session, user):
    new_user = UserFactory.build()
    new_user.email = user.email

    with pytest.raises(HTTPException) as exc_info:
        user_service.create_user(session, new_user)

    assert exc_info.value.status_code == HTTPStatus.BAD_REQUEST
    assert exc_info.value.detail == 'Username or e-mail already exists'


def test_detail_user_service(session, user):
    db_user = user_service.detail_user(session, user)
    assert db_user == user


def test_detail_user_not_exist_user_service(session):
    user = UserFactory.build()
    with pytest.raises(HTTPException) as exc_info:
        user_service.detail_user(session, user)

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND
    assert exc_info.value.detail == 'User not found'


def test_list_users_service(session, user):
    users = user_service.list_users(session)
    assert len(users) == 1


def test_update_user_service(session, user):
    user.username = 'testtest'
    user.email = 'test@mail.com'
    user.password = '1234'
    user.profile_picture = 'https://teste.com'
    updated_user = user_service.update_user(session, user)
    assert user == updated_user


def test_update_user_not_exist_user_service(session):
    user = UserFactory.build()
    with pytest.raises(HTTPException) as exc_info:
        user_service.update_user(session, user)

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND
    assert exc_info.value.detail == 'User not found'


def test_delete_user(session, user):
    user_service.delete_user(session, user)


def test_delete_user_not_exist_user_service(session):
    user = UserFactory.build()
    with pytest.raises(HTTPException) as exc_info:
        user_service.delete_user(session, user)

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND
    assert exc_info.value.detail == 'User not found'
