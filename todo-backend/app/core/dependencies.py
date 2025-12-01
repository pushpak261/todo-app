
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.config import settings
from app.schemas.auth_schema import TokenData
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserInDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_user_repo() -> UserRepository:
    return UserRepository()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: UserRepository = Depends(get_user_repo),
) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception
    user = user_repo.get_by_id(token_data.user_id)
    if user is None:
        raise credentials_exception
    return user
