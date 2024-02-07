from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


CONN = "sqlite:///sistema.db"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Cadastro(Base):
    __tablename__ = "cadastro"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(20))
    senha = Column(String(255))


try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)
