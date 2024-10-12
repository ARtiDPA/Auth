"""Файл для работы с базой данных."""
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .auth.hash import hashed
from .config import pgsqlsettings, redissettings
from .models import Base, User


class PostgresDataBase():
    """Файл для работь с бд."""

    def __init__(self) -> None:
        """Init func."""
        self.dsn = '{driver}://{user}:{password}@{host}:{port}/{name}'.format(
            driver=pgsqlsettings.db_driver,
            name=pgsqlsettings.db_name,
            password=pgsqlsettings.db_password,
            host=pgsqlsettings.db_host,
            port=pgsqlsettings.db_port,
            user=pgsqlsettings.db_user,
        )

        self.engine = create_engine(self.dsn)

    def create_all_tables(self) -> bool:
        """Создание таблиц в бд.

        Returns:
            bool: статус выполнения функции.
        """
        try:
            Base.metadata.create_all(self.engine)
        except Exception:
            return False
        return True

    def found_user(self, login) -> bool:
        """Поиск пользователя по логину в бд.

        Args:
            login (str): логин пользователя

        Returns:
            bool: True если есть пользователь, иначе False
        """
        with Session(self.engine) as connect:
            user = connect.query(User).filter(User.login == login).first()
            if user is None:
                return True
        return False

    def create_acaunt(self, login, password) -> None:
        """Создания акаунта пользователя.

        Args:
            login (str): логин пользователя
            password (str): пароль
        """
        hashed_password = hashed.create_hash(password)
        user = User(login=login, password=hashed_password)
        with Session(self.engine) as connect:
            connect.add(user)
            connect.commit()
            connect.refresh(user)


class RedisClient():
    """Класс для работы с Redis."""

    def __init__(self):
        """Init fucn."""
        self.redis_client = Redis(
            host=redissettings.redis_host,
            port=redissettings.redis_port,
            db=redissettings.redis_db,
        )


pgsql = PostgresDataBase()
