from intUtilx.models import Etiquetas, Processos, Andamentos
from intUtilx.utils import create_engine_sql

# Create sql connection with default settings
engine = create_engine_sql()

# Gerar 2 modelos
print("Gerando modelos...")
print("    Gerando etiquetas...")
Etiquetas.__table__.create(engine)
print("    Gerando processos...")
Processos.__table__.create(engine)
print("    Gerando andamentos...")
Andamentos.__table__.create(engine)
print("Modelos gerados")