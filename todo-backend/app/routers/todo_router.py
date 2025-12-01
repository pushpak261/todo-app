from fastapi import APIRouter, Depends
from typing import List
from app.schemas.todo_schema import TodoCreate, TodoPublic, TodoUpdate
from app.services.todo_service import TodoService
from app.repositories.todo_repository import TodoRepository
from app.core.dependencies import get_current_user
from app.schemas.user_schema import UserInDB

router = APIRouter(prefix="/todos", tags=["todos"])

def get_todo_service() -> TodoService:
    return TodoService(TodoRepository())

@router.get("/", response_model=List[TodoPublic])
def list_todos(
    current_user: UserInDB = Depends(get_current_user),
    service: TodoService = Depends(get_todo_service),
):
    return service.list_todos(current_user.id)

@router.post("/", response_model=TodoPublic)
def create_todo(
    todo: TodoCreate,
    current_user: UserInDB = Depends(get_current_user),
    service: TodoService = Depends(get_todo_service),
):
    return service.create_todo(current_user.id, todo)

@router.patch("/{todo_id}", response_model=TodoPublic)
def update_todo(
    todo_id: str,
    todo_update: TodoUpdate,
    current_user: UserInDB = Depends(get_current_user),
    service: TodoService = Depends(get_todo_service),
):
    return service.update_todo(current_user.id, todo_id, todo_update)

@router.delete("/{todo_id}", status_code=204)
def delete_todo(
    todo_id: str,
    current_user: UserInDB = Depends(get_current_user),
    service: TodoService = Depends(get_todo_service),
):
    service.delete_todo(current_user.id, todo_id)
    return
