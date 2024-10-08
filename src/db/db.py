"""Файл для работы с базой данных."""
from sqlalchemy import create_engine

from .config import dbsettings
from .models import Base


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

    def create_all_tables(self) -> None:
        """Создание таблиц в бд.

        Returns:
            bool: статус выполнения функции.
        """
        try:
            Base.metadata.create_all(self.engine)
        except Exception:
            return False
        return True


pgsql = PgsSql()
