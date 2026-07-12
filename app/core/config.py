from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str
    MAX_AI_RECOMMENDATIONS: int = 1
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str = "deepseek/deepseek-chat-v3"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()