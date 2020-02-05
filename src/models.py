from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('andamentos_id', Integer, ForeignKey('andamentos.id')),
    Column('etiquetas_id', Integer, ForeignKey('etiquetas.id'))
)

class Processos(Base):
    __tablename__ = 'processos'
    id = Column(Integer, primary_key=True)
    npu = Column(String)
    estado = Column(String)
    spider = Column(String)
    juiz = Column(String)
    data_distribuicao = Column(Date)
    data_captura = Column(Date)
    children = relationship("Andamentos")


class Andamentos(Base):
    __tablename__ = 'andamentos'
    id = Column(Integer, primary_key=True)
    texto = Column(String)
    bool_cinema = Column(Boolean)
    data = Column(Date)
    processos_id = Column(Integer, ForeignKey('etiquetas.id'))
    children = relationship("Etiquetas",
                            secondary=association_table)


class Etiquetas(Base):
    __tablename__ = 'etiquetas'
    id = Column(Integer, primary_key=True)
    cor = Column(String)