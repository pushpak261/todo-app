

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    password = password[:72]  
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict, expires_minutes: int = None) -> str:
    to_encode = data.copy()
    if expires_minutes is None:
        expires_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
