import csv

from intUtilx.utils import create_engine_sql

engine = create_engine_sql()

result_set = engine.execute("select * from processos")
with open('../dumps/processos.csv', 'w') as myfile:
    writer = csv.writer(myfile, delimiter='|', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
    for r in result_set:
        writer.writerow(list(r))

result_set = engine.execute("select * from etiquetas")
with open('../dumps/etiquetas.csv', 'w') as myfile:
    writer = csv.writer(myfile, delimiter='|', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
    for r in result_set:
        writer.writerow(list(r))

result_set = engine.execute("select * from andamentos")
with open('../dumps/andamentos.csv', 'w') as myfile:
    writer = csv.writer(myfile, delimiter='|', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
    for r in result_set:
        writer.writerow(list(r))
