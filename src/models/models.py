"""Описание модели."""
from sqlalchemy import DateTime, Integer, MetaData, String
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
    login: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String)
    mail: Mapped[str] = mapped_column(String, nullable=True)
    number: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[int] = mapped_column(DateTime, nullable=True)
