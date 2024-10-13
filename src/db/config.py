"""Файл конфигураций."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseServisSettings(BaseSettings):
    """Настройки сервиса.

    Args:
        BaseSettings (class): базовые настройки.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


class PgSqlSettingsq(BaseServisSettings):
    """Валидация данных для PostgreSQL.

    Args:
        BaseServisSettings (class): Настройки сервиса.
    """

    db_host: str
    db_password: str
    db_port: int
    db_shema: str
    db_name: str
    db_user: str
    db_driver: str


class RedisSettings(BaseServisSettings):
    """Валидация данных для Redis.

    Args:
        BaseServisSettings (class): Настройки сервиса.
    """

    redis_host: str
    redis_port: str
    redis_db: str


class JwtSettings(BaseServisSettings):
    """Валидация данных для JWT токенов.

    Args:
        BaseServisSettings (class): Настройки сервиса.
    """

    JWT_SEKRET_KEY: str
    ALGORITM: str
    ACCESS_TIME: int
    REFRESH_TIME: int


pgsqlsettings = PgSqlSettingsq()
redissettings = RedisSettings()
jwtsettings = JwtSettings()
