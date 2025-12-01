from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.schemas.user_schema import UserPublic, UserInDB

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserPublic)
def get_me(current_user: UserInDB = Depends(get_current_user)):
    return UserPublic(id=current_user.id, email=current_user.email, full_name=current_user.full_name)


