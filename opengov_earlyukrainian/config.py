from functools import lru_cache
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)
    openai_api_key: SecretStr = Field(default=SecretStr("sk-..."))
    log_level: str = Field(default="INFO")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

