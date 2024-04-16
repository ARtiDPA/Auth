"""Описание модели."""
from datetime import date

from sqlalchemy import Date, Integer, MetaData, String
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
    # Использую 254 потому что адрес почты не должен превышать 254 символа
    mail: Mapped[str] = mapped_column(String(254))  # noqa: WPS432
    number: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    surname: Mapped[str] = mapped_column(String(100), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=True)
    role: Mapped[int] = mapped_column(Integer)


class Role(Base):
    """Описание модели роли.

    Args:
        Base (class): базовый класс
    """

    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    access_level: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
