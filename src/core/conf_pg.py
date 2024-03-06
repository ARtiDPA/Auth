from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings_pgsql(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def data_base_pgsql(self):
        return f"""postgresql+psycopg2://
        {self.DB_USER}:
        {self.DB_PASSWORD}@
        {self.DB_HOST}:
        {self.DB_PORT}/
        {self.DB_NAME}"""  # возращают ссылку на движек для работы с БД

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings_pgsql()
