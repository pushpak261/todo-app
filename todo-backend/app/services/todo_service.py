from typing import List
from fastapi import HTTPException
from app.repositories.todo_repository import TodoRepository
from app.schemas.todo_schema import TodoCreate, TodoPublic, TodoUpdate

class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    def create_todo(self, user_id: str, todo: TodoCreate) -> TodoPublic:
        created = self.todo_repo.create_for_user(user_id, todo)
        return TodoPublic(id=created.id, title=created.title, completed=created.completed)

    def list_todos(self, user_id: str) -> List[TodoPublic]:
        todos_in_db = self.todo_repo.list_for_user(user_id)
        return [TodoPublic(id=t.id, title=t.title, completed=t.completed) for t in todos_in_db]

    def update_todo(self, user_id: str, todo_id: str, todo_update: TodoUpdate) -> TodoPublic:
        updated = self.todo_repo.update_for_user(todo_id, user_id, todo_update)
        if not updated:
            raise HTTPException(status_code=404, detail="Todo not found")
        return TodoPublic(id=updated.id, title=updated.title, completed=updated.completed)
    
    def delete_todo(self, user_id: str, todo_id: str) -> None:
        deleted = self.todo_repo.delete_for_user(todo_id, user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Todo not found")
