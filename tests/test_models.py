from tests.factories import BookFactory, NovelistFactory, UserFactory


def test_create_user(session):
    user = UserFactory.build()
    session.add(user)
    session.commit()


def test_create_novelist(session):
    novelist = NovelistFactory.build()
    session.add(novelist)
    session.commit()


def test_create_book(novelist, session):
    book = BookFactory.build(novelist_id=novelist.id)
    session.add(book)
    session.commit()
