import json
from pymongo import MongoClient

client = MongoClient('localhost',
                     port=27017,
                     username='root',
                     password='Testeintelivix2020!',
                     authSource='admin')

db = client['intelivix']

my_collection = db['my_collection']
for item in db.my_collection.find():
    print(item)
client.close()