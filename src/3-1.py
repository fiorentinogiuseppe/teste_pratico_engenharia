from sqlalchemy import create_engine
from models import Etiquetas, Processos, Andamentos
engine = create_engine('postgresql+psycopg2://postgres:Testeintelivix2020!@localhost:15432/postgres')

# Gerar 2 modelos
print("Gerando modelos...")
print("    Gerando etiquetas...")
Etiquetas.__table__.create(engine)
print("    Gerando processos...")
Processos.__table__.create(engine)
print("    Gerando andamentos...")
Andamentos.__table__.create(engine)
print("Modelos gerados")