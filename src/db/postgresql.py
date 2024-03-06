from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from core import conf_pg

Base_pgsql = declarative_base()

engine_pgsql = create_engine(url=conf_pg.settings)
