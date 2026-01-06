from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(
        default="LearnPath AI",
        description="Application name (optional, has default)"
    )
    APP_VERSION: str = Field(
        default="1.0.0",
        description="Application version (optional, has default)"
    )
    GEMINI_API_KEY: str = Field(
        ...,
        description="Gemini API key (required, no default, must be set in .env file)"
    )
    GEMINI_MODEL: str = Field(
        default="gemini-2.5-flash",
        description="Gemini model to use (optional, has default)"
    )
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Logging level (optional, has default)"
    )
    LOG_FORMAT: str = Field(
        default="%(asctime)s | %(levelname)-8s | %(module)s:%(funcName)s:%(lineno)d - %(message)s",
        description="Default log format (can be customized if needed)"
    )
    LOG_DATE_FORMAT: str = Field(
        default="%Y-%m-%d %H:%M:%S",
        description="Date/time format for logs"
    )
    LOG_TO_FILE: bool = Field(
        default=False,
        description="If true, enable logging to a file"
    )
    LOG_FILE_PATH: str = Field(
        default="logs/app.log",
        description="Path to log file"
    )
    LOG_FILE_ROTATION: str = Field(
        default="midnight",
        description="Log file rotation interval"
    )
    LOG_FILE_RETENTION: int = Field(
        default=7,
        description="Number of days to retain log files"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()