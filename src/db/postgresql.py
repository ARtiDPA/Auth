from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from ..core.conf_pg import settings

Base_pgsql = declarative_base()

engine_pgsql = create_engine(url=settings)


print(engine_pgsql)
