from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, UserPublic
from app.schemas.auth_schema import LoginRequest, Token
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service() -> AuthService:
    return AuthService(UserRepository())

@router.post("/signup", response_model=UserPublic)
def signup(user: UserCreate, service: AuthService = Depends(get_auth_service)):
    return service.signup(user)

@router.post("/login", response_model=Token)
def login(data: LoginRequest, service: AuthService = Depends(get_auth_service)):
    return service.login(data)
