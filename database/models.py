from sqlalchemy import Column, Integer, BigInteger,Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ArquiveProcess(Base):
    __tablename__ = 'arquiveprocess'
    id = Column(Integer, primary_key=True, autoincrement=True)  
    cpf = Column(BigInteger)
    private = Column(BigInteger)
    incomplet = Column(BigInteger)
    date_last_buy = Column(String)
    avarage_ticket =  Column(Float)
    ticket_last_buy = Column(Float)
    most_frequency_store = Column(BigInteger)
    store_last_buy = Column(BigInteger)
