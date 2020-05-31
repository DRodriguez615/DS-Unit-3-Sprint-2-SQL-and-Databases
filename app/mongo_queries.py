# app/mongo_queries.py

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


db = client.dspt5_db # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.dspt5_pokemon_collection # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "fav_icecream_flavors":["vanilla_bean", "choc"],
    "stats": {"a":1, "b":2, "c":[1,2,3]}
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))





mewtwo = {
    "name": "Mewtwo",
    "level": 100,
    "exp": 76000000000,
    "hp": 450,
    "strength": 550,
    "intelligence": 450,
    "dexterity": 300,
    "wisdom": 575
}

pikachu = {
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
}

blastoise = {
    "name": "Blastoise",
    "lvl": 70,
}

skarmory = {
    "name": "Skarmory",
    "level": 22,
    "exp": 42000,
    "hp": 85,
    "strength": 750,
    "intelligence": 8,
    "dexterity": 57
}

cubone = {
    "name": "Cubone",
    "level": 20,
    "exp": 35000,
    "hp": 80,
    "strength": 600,
    "intelligence": 60,
    "dexterity": 200,
    "wisdom": 200
}
pokemon_team = [mewtwo, pikachu, blastoise, skarmory, cubone]
collection.insert_many(pokemon_team)

print("DOCS:", collection.count_documents({}))

pikas = list(collection.find({"name": "Pikachu"}))
print(len(pikas), "PIKAS")

print(pikas[0]["_id"])
print(pikas[0]["name"])