"""Модели на sqlalhemy для pgsql."""
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db import postgresql


class User(postgresql.Base_pgsql):
    """Модель пользователя.

    Args:
        postgresql (config): Базовый декларотивный класс.
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    mail: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    passwrod: Mapped[str] = mapped_column(String)
