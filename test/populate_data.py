import json
from pymongo import MongoClient

client = MongoClient('localhost',
                     port=27017,
                     username='root',
                     password='Testeintelivix2020!',
                     authSource='admin')

db = client['intelivix']

my_collection = db['my_collection']
print(my_collection)

with open('../datasets/dataset-6.json') as f:
    file_data = json.load(f)
print(file_data)
#my_collection.insert_many(file_data)
my_collection.insert_one(file_data)
client.close()