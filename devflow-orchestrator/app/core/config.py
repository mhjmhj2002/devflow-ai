from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Agentic Platform"

    GITHUB_TOKEN: str = ""
    GITHUB_OWNER: str = ""

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"

    DEBUG: bool = True


settings = Settings()