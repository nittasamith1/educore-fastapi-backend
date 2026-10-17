from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class DatabaseSettings(BaseAppSettings):
    DATABASE_URL: str


class SecuritySettings(BaseAppSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str


settings = DatabaseSettings()
sec_settings = SecuritySettings()