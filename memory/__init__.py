"""
Memory module for managing chat conversation history

Provides:
    - ChatHistory: Protocol defining the storage interface
    - ChatMemory: Simple in-memory implementation

Designed for easy dependency injection and future extension (Redis, database, etc.)
"""

from .chat_history import ChatHistory
from .chat_memory import ChatMemory

__all__ = ["ChatHistory", "ChatMemory"]
