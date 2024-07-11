from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "***",
    server_api=ServerApi('1')
)

db = client.book

def show_all():
    result = db.cats.find({})
    for el in result:
        print(el)

def show(name: str):
    try:
        result = db.cats.find_one({"name": name})
    except Exception as e:
        print("Name not found")
    print(result)

def update_age(name: str, age: int):
    try:
        db.cats.update_one({"name": name}, {"$set": {"age": age}})
    except Exception as e:
        print("Name not found")
    print("Age is update now")
    result = db.cats.find_one({"name": name})
    print(result)

def update_features(name: str, features: str):
    try:
        db.cats.update_one({"name": name}, {"$push": {"features": features}})
    except Exception as e:
        print("Name not found")
    print("Features is update now")
    result = db.cats.find_one({"name": name})
    print(result)

def delete_one(name: str):
    try:
        db.cats.delete_one({"name": name})
    except Exception as e:
        print("Name not found")
    print(f"{name} deleted")
    show_all()

def delete_all():
    db.cats.delete_many({})
    print("Everyone deleted")


