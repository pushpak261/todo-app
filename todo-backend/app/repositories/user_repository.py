from typing import Optional
from bson import ObjectId
from app.db.mongodb import users_collection
from app.schemas.user_schema import UserCreate, UserInDB
from app.core.security import hash_password

class UserRepository:
    def create_user(self, user: UserCreate) -> UserInDB:
        doc = {
            "email": user.email,
            "full_name": user.full_name,
            "password_hash": hash_password(user.password),
        }
        result = users_collection.insert_one(doc)
        return UserInDB(
            id=str(result.inserted_id),
            email=user.email,
            full_name=user.full_name,
            password_hash=doc["password_hash"],
        )

    def get_by_email(self, email: str) -> Optional[UserInDB]:
        doc = users_collection.find_one({"email": email})
        if not doc:
            return None
        return UserInDB(
            id=str(doc["_id"]),
            email=doc["email"],
            full_name=doc.get("full_name"),
            password_hash=doc["password_hash"],
        )

    def get_by_id(self, user_id: str) -> Optional[UserInDB]:
        doc = users_collection.find_one({"_id": ObjectId(user_id)})
        if not doc:
            return None
        return UserInDB(
            id=str(doc["_id"]),
            email=doc["email"],
            full_name=doc.get("full_name"),
            password_hash=doc["password_hash"],
        )
