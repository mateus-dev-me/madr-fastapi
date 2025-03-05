from sqlalchemy import func, select

from madr.database.models import User
from madr.repositories import user_repository
from tests.factories import UserFactory


def test_create_user_repository(session):
    new_user = UserFactory.build()
    created_user = user_repository.create_user(session, new_user)
    count = session.scalar(select(func.count()).select_from(User))
    assert new_user.username == created_user.username
    assert new_user.email == created_user.email
    assert count == 1


def test_get_user_by_id_repository(session, user):
    db_user = user_repository.get_user_by_id(session, user.id)
    assert db_user is not None
    assert db_user == user


def test_list_users_repository(session, user):
    users = user_repository.list_users(session)
    assert len(users) == 1


def test_update_user_repository(session, user):
    user.username = 'testtest'
    user.email = 'test@mail.com'
    user.password_hash = 'test1235'
    user.profile_picture = 'https://testeimage.com'
    updated_user = user_repository.update_user(session, user)
    assert updated_user == user


def test_delete_user_repository(session, user):
    user_repository.delete_user(session, user)
    deleted_user = session.get(User, user.id)
    assert deleted_user is None


def test_get_user_by_username_or_email_repository(session, user):
    db_user = user_repository.get_user_by_username_or_email(
        session, user.username, user.email
    )
    assert db_user is not None
    assert db_user == user
