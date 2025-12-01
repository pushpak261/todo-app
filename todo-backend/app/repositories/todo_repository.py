

from typing import List, Optional
from bson.objectid import ObjectId
from app.db.mongodb import todos_collection
from app.schemas.todo_schema import TodoCreate, TodoInDB, TodoUpdate

class TodoRepository:
    def create_for_user(self, user_id: str, todo: TodoCreate) -> TodoInDB:
        doc = {
            "title": todo.title,
            "completed": todo.completed,
            "user_id": user_id,
        }
        result = todos_collection.insert_one(doc)
        return TodoInDB(id=str(result.inserted_id), user_id=user_id, **todo.dict())

    def list_for_user(self, user_id: str) -> List[TodoInDB]:
        docs = todos_collection.find({"user_id": user_id})
        return [
            TodoInDB(
                id=str(d["_id"]),
                user_id=d["user_id"],
                title=d["title"],
                completed=d["completed"],
            )
            for d in docs
        ]

    def get_by_id_for_user(self, todo_id: str, user_id: str) -> Optional[TodoInDB]:
        doc = todos_collection.find_one({"_id": ObjectId(todo_id), "user_id": user_id})
        if not doc:
            return None
        return TodoInDB(
            id=str(doc["_id"]),
            user_id=doc["user_id"],
            title=doc["title"],
            completed=doc["completed"],
        )
    
    def delete_for_user(self, todo_id: str, user_id: str) -> bool:
        res = todos_collection.delete_one({"_id": ObjectId(todo_id), "user_id": user_id})
        return res.deleted_count == 1

    def update_for_user(self, todo_id: str, user_id: str, todo_update: TodoUpdate) -> Optional[TodoInDB]:
        update_data = {k: v for k, v in todo_update.dict().items() if v is not None}
        if not update_data:
            return self.get_by_id_for_user(todo_id, user_id)
        todos_collection.update_one(
            {"_id": ObjectId(todo_id), "user_id": user_id},
            {"$set": update_data},
        )
        return self.get_by_id_for_user(todo_id, user_id)


