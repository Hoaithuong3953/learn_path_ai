"""
Domain layer for LearnPath chatbot

Key features:
- Re-export Resource, Milestone, Roadmap, UserProfile, ChatMessage from models
- Independent of application and infrastructure layers
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