"""
Configuration module for LearnPath chatbot

Key features:
- settings: singleton Settings instance (from .env)
- Settings: Pydantic settings class for GEMINI_* and LOG_*
"""

from .settings import settings, Settings

__all__ = ["settings", "Settings"]
