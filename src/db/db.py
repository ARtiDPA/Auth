"""Файл для работы с базой данных."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .config import dbsettings
from .models import Base, User


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
        with Session(self.engine) as connect:
            user = connect.query(User).filter(User.login == login).first()
            if user is None:
                return True
        return False


    def create_acaunt(self, login, password):
        if self.found_user(login):
            user = User(login=login, password=password)
            with Session(self.engine) as connect:
                connect.add(user)
                connect.commit()
                connect.refresh(user)


pgsql = PgsSql()
