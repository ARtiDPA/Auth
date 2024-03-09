"""Настройки."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsPGsql(BaseSettings):
    """Настройки ссылки.

    Args:
        BaseSettings (config): Базовый декларативный класс.

    Returns:
        : Ссылка на движёк для работы с бд
    """

    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    def data_base_pgsql(self) -> str:
        """Создание ссылки.

        Args:
            None

        Returns:
            str: Ссылка на движек.
        """
        link_engine = """asyncpg://
            {db_user}:
            {db_password}@
            {db_host}:
            {db_port}/
            {db_name}"""

        link_engine.format(
            db_user=self.db_user,
            db_password=self.db_password,
            db_host=self.db_host,
            db_port=self.db_port,
            db_name=self.db_name,
            )

        return link_engine

    model_config = SettingsConfigDict(env_file='.env')


settings_pgsql = SettingsPGsql()
