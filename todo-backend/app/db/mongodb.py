from pymongo import MongoClient
from app.config import settings
import certifi

client = MongoClient(settings.MONGODB_URI, tls=True, tlsCAFile=certifi.where())
db = client[settings.MONGODB_DB_NAME]

users_collection = db["users"]
todos_collection = db["todos"]
