from pymongo import MongoClient
from Mongo_Defs import *

def to_mongo(person_dict):
    client = MongoClient("mongodb://Denis:vdpass@cluster0-shard-00-00.l1f8y.mongodb.net:27017,cluster0-shard-00-01.l1f8y.mongodb.net:27017,cluster0-shard-00-02.l1f8y.mongodb.net:27017/vd_db?ssl=true&replicaSet=atlas-5ltqw8-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.vd_db
    collection = db.vd_telegram_bot
    _id = insert_document(collection, person_dict)
