from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from madr.core.config import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():  # pragma: no cover
    """
    Gera uma sessão do SQLAlchemy e garante seu fechamento automático.

    Yields:
        Session: uma sessão ativa para interagir com o banco de dados.
    """
    with Session(engine) as session:
        yield session
