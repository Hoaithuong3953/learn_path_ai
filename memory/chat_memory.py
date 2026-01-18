from typing import List
from datetime import datetime

from domain.models import ChatMessage
from memory.chat_history import ChatHistory

class ChatMemory:
    """
    Responsibilities:
    - Store chat history in memory
    - Provide methods to add and retrieve messages
    """
    def __init__(self, storage: List[ChatMessage]):
        """Initialize chat memory with storage"""
        self.storage = storage

    def load_history(self) -> List[ChatMessage]:
        """Load chat history from storage"""
        return self.storage

    def add_message(self, message: ChatMessage) -> None:
        """Format and append a message to the chat history"""
        self.storage.append(message)
    
    def add_user_message(self, content: str) -> None:
        """Add a user message to the chat history"""
        message = ChatMessage(
            role="user",
            content=content,
            timestamp=datetime.now()
        )
        self.add_message(message)
    
    def add_bot_message(self, content: str) -> None:
        """Add a bot message to the chat history"""
        message = ChatMessage(
            role="assistant",
            content=content,
            timestamp=datetime.now()
        )
        self.add_message(message)

    def clean_history(self):
        """Clear the chat history"""
        self.storage.clear()