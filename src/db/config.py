"""Файл конфигураций."""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class PgSqlSettingsq(BaseSettings):
    """Настройки для работы с базой данных.

    Args:
        BaseSettings (class): базовые настройки.
    """

    model_config = SettingsConfigDict(env_file='.env')
    db_host: str
    db_password: str
    db_port: int
    db_shema: str
    db_name: str
    db_user: str
    db_driver: str


dbsettings = PgSqlSettingsq()
