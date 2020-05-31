import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print(dir(client))
print("DB NAMES:", client.list_database_names())


db = client.dspt5_rpg_db # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.armory_items # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

Libero_facere_dolore_as = {
    "item_id": 1,
    "name": "Libero facere dolore_as",
    "value": 0,
    "weight": 0
}

qui = {
    "item_id": 2,
    "name": "Qui",
    "value": 0,
    "weight": 0,
}

Laborios = {
    "item_id": 3,
    "name": "Laborios",
    "value": 0,
    "weight": 0
}

Quibusdam_illo_deserunt_ea = {
    "item_id": 4,
    "name": "Quibusdam illo deserunt ea",
    "value": 0,
    "weight": 0,
}

quod_eveniet_i  = {
    "item_id": 5,
    "name": "Quod eveniet i",
    "value": 0,
    "weight": 0,
}
armory_item = [Libero_facere_dolore_as, qui, Laborios, Quibusdam_illo_deserunt_ea, quod_eveniet_i ]
collection.insert_many(armory_item)

print("DOCS:", collection.count_documents({}))