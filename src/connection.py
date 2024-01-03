from pymongo import MongoClient

client = MongoClient("mongodb://user:name@localhost:27017/")

db = client.dio_live

trends_collection = db.trends
