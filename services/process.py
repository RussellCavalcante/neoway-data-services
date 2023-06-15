from sqlalchemy.future import select
from sqlalchemy import delete , text

from database.models import ArquiveProcess
from database.connection import async_session
from database.connection import engine


class ProcessingService:
    def create_processment(*args, **kwargs):
        
        connection = engine.connect()
        with connection as session:

            query = text(f"""INSERT INTO arquiveprocess 
                         (cpf, private, incomplet, date_last_buy, avarage_ticket, ticket_last_buy, most_frequency_store, store_last_buy)
                          VALUES ({args[0]}, {args[1]}, {args[2]}, {args[3]}, {args[4]}, {args[5]}, {args[6]} , {args[7]} );""")
            session.execute(query)
            session.commit()
            # rows = result.fetchall()
            # for row in rows:
            #     print(row)
            #     input()
        connection.close()