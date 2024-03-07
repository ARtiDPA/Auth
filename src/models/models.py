from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from db import postgresql


class user(postgresql.Base_pgsql):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    mail: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    passwrod: Mapped[str] = mapped_column(String)


class roles(postgresql.Base_pgsql):

    __tablename__ = "role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
