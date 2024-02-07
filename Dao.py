from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from Model import *


def getSession():

    CONN = "sqlite:///sistema.db"

    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()


class CadastroDao:
    @classmethod
    def cadastrar(cls, cadastro: Cadastro):
        session = getSession()

        x = session.query(Cadastro).filter_by(email=cadastro.email).all()

        if len(x) == 0:
            c = Cadastro(nome=cadastro.nome, email=cadastro.email, senha=cadastro.senha)

            session.add(c)
            session.commit()

            return c

        else:
            return None


class LoginDao:
    @classmethod
    def acesso(cls, cadastro: Cadastro):
        session = getSession()

        c = (
            session.query(Cadastro)
            .filter_by(email=cadastro.email, senha=cadastro.senha)
            .all()
        )

        if len(c) > 0:
            return c[0]
        else:
            return None
