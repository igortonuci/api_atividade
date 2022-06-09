from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#tabela pessoas
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    #quando pedir para imprimir o obj vai imprimir nessa função
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

#tabela atividade
class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer,primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")



    def init_db():
        Base.metadata.create_all(bind=engine)

    if __name__ == '__main__':
        init_db()

