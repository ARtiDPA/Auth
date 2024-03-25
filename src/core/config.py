"""Файл настроек."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки бд.

    Args:
        BaseSettings (class): базовые настройки
    """

    model_config = SettingsConfigDict(env_file='.env')

    db_driver: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    db_schema: str


database_settings = DatabaseSettings()
