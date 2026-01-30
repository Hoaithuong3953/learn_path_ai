"""
Protocol defining the chat history storage interface

Any class implementing these two methods can be use as chat history backend
"""

from typing import Protocol, List

from domain import ChatMessage

class ChatHistory(Protocol):
    """
    Interface for chat history storage
    """
    def add_message(self, message: ChatMessage) -> None:
        """
        Add a message to chat history
        """
        ...

    def load_history(self) -> List[ChatMessage]:
        """
        Retrieve full chat history
        """
        ...