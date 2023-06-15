from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DATABASE_URL = 'postgresql://admin:admin@localhost:5432/neowaydb'
DATABASE_URL_ASYNC = 'postgresql+asyncpg://admin:admin@localhost:5432/neowaydb'

engine_async = create_async_engine(DATABASE_URL_ASYNC)
engine = create_engine(DATABASE_URL)


async_session = sessionmaker(engine, class_=AsyncSession)
