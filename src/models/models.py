"""Описание модели."""
from sqlalchemy import Integer, MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.config import database_settings


class Base(DeclarativeBase):
    """Описание базового класса.

    Args:
        DeclarativeBase (clas): базовый декларативный класс
    """

    metadata = MetaData(schema=database_settings.db_schema)


class User(Base):
    """Описание модели пользователя.

    Args:
        Base (class): базовый класс
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    mail: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
