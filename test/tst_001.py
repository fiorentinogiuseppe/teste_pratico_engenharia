from sqlalchemy import create_engine
from collections import Counter
from pymongo import MongoClient
from copy import deepcopy

def insertDB():
    engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'Joe', balance = 100)


def get_processos(item):
    item = deepcopy(item)
    item.pop('andamentos', None)
    print(item)


def get_andamentos(item):
    item = deepcopy(item)
    for i in item['andamentos']:
        i.pop('etiquetas', None)
        print(i)


def get_etiquetas(item):
    etiquetas = []
    for i in item['andamentos']:
        etiquetas+= i['etiquetas']
    etiquetas = list(set(etiquetas))
    print(etiquetas)


def miningData(item):
    get_processos(item)
    print("\n\n")
    get_andamentos(item)
    print("\n\n")
    get_etiquetas(item)


engine = create_engine('postgresql+psycopg2://postgres:Testeintelivix2020!@localhost:15432/postgres')
client = MongoClient('localhost',
                     port=27017,
                     username='root',
                     password='Testeintelivix2020!',
                     authSource='admin')

db = client['intelivix']

my_collection = db['my_collection']

for item in my_collection.find():
    miningData(item)
    break


