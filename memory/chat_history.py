from typing import Protocol, List

from domain.models import ChatMessage

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
        Load full chat history
        """
        ...