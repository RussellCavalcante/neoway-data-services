from asyncio import run
from database.init_db import create_database

if __name__ == '__main__':
    run(create_database())
