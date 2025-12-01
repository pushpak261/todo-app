
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserPublic, UserInDB
from app.schemas.auth_schema import LoginRequest, Token
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def signup(self, user_data: UserCreate) -> UserPublic:
        existing = self.user_repo.get_by_email(user_data.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        created = self.user_repo.create_user(user_data)
        return UserPublic(id=created.id, email=created.email, full_name=created.full_name)

    def login(self, login_data: LoginRequest) -> Token:
        user = self.user_repo.get_by_email(login_data.email)
        if not user or not verify_password(login_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        token = create_access_token({"sub": user.id})
        return Token(access_token=token)
