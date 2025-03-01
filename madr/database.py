from sqlalchemy import Session, create_engine

from madr.core.config import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    """
    Gera uma sessão do SQLAlchemy e garante seu fechamento automático.

    Yields:
        Session: uma sessão ativa para interagir com o banco de dados.
    """
    with Session(engine) as session:
        yield session
