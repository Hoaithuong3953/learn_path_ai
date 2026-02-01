"""
chat_history.py

Protocol defining the required interface for any chat history storage

Key features:
- add_message, load_history, clean_history: contract for chat history backends
- Enables swapping implementations (in-memory, Redis, database)
"""

from typing import Protocol, List

from domain import ChatMessage

class ChatHistory(Protocol):
    """
    Interface that every chat history storage must follow

    Responsibilities:
    - add_message: append a message in chronological order
    - load_history: return messages oldest-first
    - clean_history: remove all messages (e.g. new conversation or session reset)
    """
    def add_message(self, message: ChatMessage) -> None:
        """Append a new message to the end of the conversation history

        The message is added in chronological order (most recent last)
        """
        ...

    def load_history(self) -> List[ChatMessage]:
        """Return the complete list of messages in this conversation
        
        Returns messages in chronological order (oldest first)
        Implementations should return a copy or immutable view if possible
        to prevent accidental modification of internal storage
        """
        ...
    
    def clean_history(self):
        """Remove all messages from the current conversation history
        
        Used when:
        - User starts a new conversation
        - Session is being reset
        """
        ...