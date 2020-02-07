from intUtilx.utils import create_engine_sql

engine = create_engine_sql()

print("Qual o total de processos? ")
result_set = engine.execute("select count(*) from processos")
for r in result_set:
    print("R: ", r[0])

print("Qual o total de andamentos?")
result_set = engine.execute("select count(*) from andamentos")
for r in result_set:
    print("R: ", r[0])

print("Qual processo possui mais andamentos?")
result_set = engine.execute("SELECT processos.id, count(andamentos.id) FROM processos INNER JOIN andamentos ON processos.id=andamentos.processos_id GROUP BY processos.id ORDER BY COUNT(andamentos.id) DESC LIMIT 1")
for r in result_set:
    print("R: ", r[0])

print("Quais andamentos possuem mais caracteres?" "Quais são os seus processos?")
result_set = engine.execute("select id, CHARACTER_LENGTH(texto), processos_id from andamentos order by  CHARACTER_LENGTH(texto) desc limit 1")
for r in result_set:
    print("R: id {} - quantidade {} - id do processo {}".format(r[0],r[1], r[2]))

print('Qual andamento mais antigo com o termo "cinema"?')
result_set = engine.execute("select data from andamentos where bool_cinema=True order by data asc limit 1")
for r in result_set:
    print("R: ", r[0])

print('Qual processo possui o maior número formado pelos seus 6 primeiros números do seu npu?')
result_set = engine.execute("select  id, LEFT(npu, 6) from processos order by LEFT(npu, 6) desc limit 1")
for r in result_set:
    print("R: ", r[0])

print('Qual mês/ano foram capturados mais processos para cada "spider"?')
result_set = engine.execute("""
    select distinct on (dm.spider) dm.spider, dm.my, dm.count from(
	    select to_char(data_captura, 'YYYY-MM') as my, count(to_char(data_captura, 'YYYY-MM')), spider from processos group by spider, my order by spider, count desc
    ) dm
    join(
	    select spider, max(count) from(
		    select to_char(data_captura, 'YYYY-MM') as my, count(to_char(data_captura, 'YYYY-MM')), spider from processos group by spider, my order by spider, count desc
	    ) as y
	    group by spider
    ) sm
    on sm.max = dm.count and dm.spider = sm.spider
""")

for r in result_set:
    print("R: spider {} - mes/ano {} - quantidade {} ".format(r[0],r[1],r[2]))
