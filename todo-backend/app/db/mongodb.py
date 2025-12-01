
from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB_NAME]

users_collection = db["users"]
todos_collection = db["todos"]
