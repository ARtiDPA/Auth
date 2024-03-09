"""Создание движка для PgSQL."""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from src.core.config_pgsql import settings_pgsql

Base_pgsql = declarative_base()

engine_pgsql = create_engine(url=settings_pgsql)
