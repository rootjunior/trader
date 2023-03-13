from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

from settings import settings

meta = MetaData()

async_engine = create_async_engine(settings.postgresql_dsn, echo=False)
