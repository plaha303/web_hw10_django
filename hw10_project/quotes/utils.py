from pymongo import MongoClient


def get_mongo():
    client = MongoClient("mongodb://localhost:2700")

    db = client.quotes
    return db