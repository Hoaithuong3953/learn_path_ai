"""
chat_memory.py

In-memory implementation of chat history storage (list-based)

Key features:
- ChatMemory: add/load/clear messages; data lost on restart
- Suitable for testing, prototypes and short-lived sessions
"""

from typing import List
from domain import ChatMessage

class ChatMemory:
    """
    Handle in-memory chat history (add, load, clear)

    Responsibilities:
    - Store messages in an in-memory list
    - Provide add_message, add_user_message, add_bot_message, load_history, clean_history
    """
    def __init__(self, storage: List[ChatMessage]):
        """Initialize chat memory with the given storage list"""
        self.storage = storage

    def load_history(self) -> List[ChatMessage]:
        """
        Load chat history from storage

        Returns:
            List of ChatMessage in chronological order
        """
        return self.storage

    def add_message(self, message: ChatMessage) -> None:
        """
        Add a message to the chat history

        Args:
            message: ChatMessage to append
        """
        self.storage.append(message)

    def add_user_message(self, content: str) -> None:
        """
        Add a user message to the chat history

        Args:
            content: Raw text of the user message
        """
        msg = ChatMessage(role="user", content=content)
        self.add_message(msg)

    def add_bot_message(self, content: str) -> None:
        """
        Add a bot/assistant message to the chat history

        Args:
            content: Raw text of the assistant message
        """
        msg = ChatMessage(role="assistant", content=content)
        self.add_message(msg)

    def clean_history(self) -> None:
        """Clear all messages from the chat history"""
        self.storage.clear()