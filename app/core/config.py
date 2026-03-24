from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Central configuration — values are loaded from environment variables
    or a .env file automatically by pydantic-settings.
    """

    # ── General ─────────────────────────────────────────────────────────
    APP_NAME: str = "AI Data API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # ── CORS ────────────────────────────────────────────────────────────
    ALLOWED_ORIGINS: list[str] = ["*"]

    # ── Database (ready for when you add one) ───────────────────────────
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/juniordevai"

    # ── AI Service keys (examples) ──────────────────────────────────────
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }


settings = Settings()
