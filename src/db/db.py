"""Файл для работы с базой данных."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .config import dbsettings
from .models import Base, User
from .auth.hash import hashed


class PgsSql():
    """Файл для работь с бд."""

    def __init__(self) -> None:
        """Init func."""
        self.dsn = '{driver}://{user}:{password}@{host}:{port}/{name}'.format(
            driver=dbsettings.db_driver,
            name=dbsettings.db_name,
            password=dbsettings.db_password,
            host=dbsettings.db_host,
            port=dbsettings.db_port,
            user=dbsettings.db_user,
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


pgsql = PgsSql()
