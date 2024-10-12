"""Файл моделей для бд."""
from sqlalchemy import Integer, MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .config import pgsqlsettings


class Base(DeclarativeBase):
    """Базовый класс.

    Args:
        DeclarativeBase (class): декларативный класс
    """

    metadata = MetaData(schema=pgsqlsettings.db_shema)


class User(Base):
    """Модель пользователя.

    Args:
        Base (class): базовый класс
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
