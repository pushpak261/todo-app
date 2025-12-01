from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoInDB(TodoBase):
    id: str
    user_id: str

class TodoPublic(TodoBase):
    id: str

    class Config:
       from_attributes = True

    
