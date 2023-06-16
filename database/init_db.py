

from database.connection import engine_async
from database.models import Base

async def create_database():
    async with engine_async.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all) 


    