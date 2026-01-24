"""
Domain layer for learnpath_chatbot

Contains core logic and domain models
Independent of application and infrastructure layers
"""

from .models import (
    Resource,
    Milestone,
    Roadmap,
    UserProfile,
    ChatMessage
)

__all__ = [
    "Resource",
    "Milestone",
    "Roadmap",
    "UserProfile",
    "ChatMessage"
]