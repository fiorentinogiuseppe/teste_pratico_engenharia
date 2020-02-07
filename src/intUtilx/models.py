from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Table, ARRAY
from sqlalchemy.orm import relationship

# Global variable to constructs a base class
Base = declarative_base()


class Processos(Base):
    """
        `Processos` table
    """
    __tablename__ = 'processos'
    id = Column(String, primary_key=True, autoincrement=False)
    npu = Column(String)
    estado = Column(String)
    spider = Column(String)
    juiz = Column(String)
    data_distribuicao = Column(Date)
    data_captura = Column(Date)
    children = relationship("Andamentos")


class Andamentos(Base):
    """
        `Andamentos` table
    """
    __tablename__ = 'andamentos'
    id = Column(Integer, primary_key=True)
    texto = Column(String)
    bool_cinema = Column(Boolean)
    data = Column(Date)
    processos_id = Column(String, ForeignKey('processos.id'))
    etiquetas_id = Column(Integer, ForeignKey('etiquetas.id'))


class Etiquetas(Base):
    """
        `Etiquetas` table
    """
    __tablename__ = 'etiquetas'
    id = Column(Integer, primary_key=True)
    cor = Column(ARRAY(String))
    children = relationship("Andamentos")
