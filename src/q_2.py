from collections import Counter
from intUtilx.utils import create_connection

my_collection, client = create_connection()

total_andamentos = 0
for item in my_collection.find():
    total_andamentos += len(item['andamentos'])


print("Contagem total dos processos: ",my_collection.count_documents({}))

print("Contagem total dos andamentos: ",total_andamentos)

print("\nContagem de processos por estado")

count_by_states = my_collection.aggregate([
    # Now lets group on the name counting how many grouped documents we have
    {"$group":{"_id":"$estado", "sum":{"$sum":1}}},
    # Sort ascending.
    {"$sort": {"_id": 1}}
])
for states_count in count_by_states:
    print("O estado de {} tem um total de {} processos".format(states_count['_id'], states_count['sum']))

# for case insensitive search options i

print("\nContagem de juízes que começam com 'S': ", my_collection.count_documents({"juiz": {'$regex': "^S", "$options" : "i"}}))

print("Contagem de etiquetas mais comuns: ")
list_etiquetas = [i['andamentos'][0]['etiquetas'] for i in my_collection.find({},{'andamentos.etiquetas' :1})]
Output = Counter([tuple(i) for i in list_etiquetas])
for key, value in Output.items():
    print("A Etiqueta {} teve {} ocorrencias".format(key, value))

client.close()