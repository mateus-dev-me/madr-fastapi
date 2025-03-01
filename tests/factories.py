import random

import factory
from faker import Faker

from madr.models import Book, Novelist, User

fake = Faker()


class UserFactory(factory.base.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    password_hash = factory.LazyAttribute(lambda _: fake.password())
    profile_picture = factory.LazyAttribute(lambda _: fake.image_url())


class NovelistFactory(factory.base.Factory):
    class Meta:
        model = Novelist

    name = factory.LazyAttribute(lambda _: fake.name())
    biography = factory.LazyAttribute(
        lambda _: fake.text(max_nb_chars=500)
    )  # Gerando biografia
    birth_date = factory.LazyAttribute(
        lambda _: fake.date_of_birth(minimum_age=25, maximum_age=90)
    )  # Data de nascimento
    death_date = factory.LazyAttribute(
        lambda _: fake.date_of_birth(minimum_age=25, maximum_age=90)
        if random.choice([True, False])
        else None
    )  # Data de falecimento (opcional)
    nationality = factory.LazyAttribute(
        lambda _: fake.country()
    )  # Nacionalidade
    awards = factory.LazyAttribute(
        lambda _: fake.text(max_nb_chars=200)
        if random.choice([True, False])
        else None
    )  # Premiações (opcional)
    social_media_links = factory.LazyAttribute(
        lambda _: {
            'twitter': fake.url(),
            'instagram': fake.url(),
            'facebook': fake.url(),
        }
        if random.choice([True, False])
        else None
    )  # Links de redes sociais (opcionais)


class BookFactory(factory.base.Factory):
    class Meta:
        model = Book

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=3))
    year = factory.LazyAttribute(lambda _: fake.year())
    isbn = factory.LazyAttribute(lambda _: fake.isbn13())
    pages = factory.LazyAttribute(lambda _: fake.random_int(min=50, max=1000))
    genre = factory.LazyAttribute(lambda _: fake.word())
    subgenre = factory.LazyAttribute(lambda _: fake.word())
    tropes = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=200))
    heat_level = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=5))
    target_audience = factory.LazyAttribute(lambda _: fake.word())
    publisher = factory.LazyAttribute(lambda _: fake.company())
    edition = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=10))
    published_date = factory.LazyAttribute(lambda _: fake.date_this_century())
    novelist_id = factory.SubFactory(NovelistFactory)
