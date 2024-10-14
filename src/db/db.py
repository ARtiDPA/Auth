"""Файл для работы с базой данных."""
from typing import Union

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
                return False
        return True

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

    def get_user(self, login) -> Union[User, bool]:
        """Получение пользователя.

        Args:
            login (str): данные о пользователе

        Returns:
            Union[int, bool]: [айди пользователя, False]
        """
        with Session(self.engine) as connect:
            user = connect.query(User).filter(User.login == login).first()
            return user if user else False


class RedisClient():
    """Класс для работы с Redis."""

    def __init__(self):
        """Init fucn."""
        self.redis_client = Redis(
            host=redissettings.redis_host,
            port=redissettings.redis_port,
            db=redissettings.redis_db,
        )

    def get_key(self, key: str) -> str:
        """Получения ключа из Redis.

        Args:
            key (str): ключ

        Returns:
            str: значение ключа
        """
        return self.redis_client.get(key)

    def set_key(
            self,
            key: str,
            value: str,
            time: Union[int, None] = 0,
            ) -> bool:
        """Вставка ключа в Redis.

        Args:
            key (str): ключ
            value (str): значение
            time (int | None): время жизни ключ/значения.

        Returns:
            bool: статус-код выполнения функции
        """
        return redis_client.set_key(key, value, time)


redis_client = RedisClient()
pgsql = PostgresDataBase()
