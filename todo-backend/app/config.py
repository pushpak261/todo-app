
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Todo Backend"
    MONGODB_URI: str
    MONGODB_DB_NAME: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    class Config:
        env_file = ".env"

settings = Settings()
