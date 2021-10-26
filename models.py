from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///efetivo.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Pacotes(Base):
    __tablename__ = 'pacotes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True)
    def __repr__(self):
        return '<Pacote {}>'.format(self.nome)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Disciplinas(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    def __repr__(self):
        return '<Disciplina {}>'.format(self.nome)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Efetivo(Base):
    __tablename__='efetivo'
    id = Column(Integer, primary_key=True)
    pacote_id = Column(Integer, ForeignKey('disciplinas.id'))
    pacote = relationship("Pacotes")
    data = Column(Date, index=True)
    disciplina_id = Column(Integer, ForeignKey('pacotes.id'))
    disciplina = relationship("Disciplinas")
    efetivo = Column(Integer)
    planejador = Column(String(40))
    observacao = Column(String(60))
    def __repr__(self):
        return '<Efetivo {}>'.format(self.nome)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()




