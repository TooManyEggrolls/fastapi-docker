from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_host: str = Field(..., env="DATABASE_HOST")
    database_name: str = Field(..., env="DATABASE_NAME")
    database_port: str = Field(..., env="DATABASE_PORT")
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")


settings = Settings()
