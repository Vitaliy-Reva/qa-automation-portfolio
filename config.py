from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str
    api_token: str
    timeout: int = 30

    class Config:
        env_file = ".env"