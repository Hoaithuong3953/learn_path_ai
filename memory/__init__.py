"""
Memory module for managing chat conversation history

Key features:
- ChatHistory: protocol for storage interface (add_message, load_history, clean_history)
- ChatMemory: in-memory implementation for DI and future extension (Redis, DB)
"""

from .chat_history import ChatHistory
from .chat_memory import ChatMemory

__all__ = ["ChatHistory", "ChatMemory"]
