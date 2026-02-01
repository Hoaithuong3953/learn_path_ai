"""
settings.py

Application configuration and environment-based settings loaded from .env

Key features:
- GEMINI_API_KEY, GEMINI_MODEL: API and model config (required/optional)
- LOG_LEVEL, LOG_TO_FILE, LOG_FILE_*: logging config and file rotation
- Validation for API key format and log retention
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import Literal

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables (.env)

    Responsibilities:
    - Load and validate GEMINI_* and LOG_* settings
    - Validate GEMINI_API_KEY (non-empty, AIzaSy prefix, length)
    - Expose APP_NAME, APP_VERSION and logging options
    """
    
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

    @field_validator('GEMINI_API_KEY')
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        """Validate API key non-empty and reasonable format (AIzaSy prefix, length)"""
        v = v.strip()

        if not v:
            raise ValueError("GEMINI_API_KEY cannot be empty")
        
        if not v.startswith("AIzaSy"):
            raise ValueError("GEMINI_API_KEY should start with 'AIzaSy'. Please check if you're using a valid Google AI Studio API key")
        
        if len(v) < 30 or len(v) > 50:
            raise ValueError(f"GEMINI_API_KEY length ({len(v)}) seems unusual. Please check your key")
        
        return v


    # Logging settings
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
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
        ge=1,
        description="Number of days to retain log files"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()