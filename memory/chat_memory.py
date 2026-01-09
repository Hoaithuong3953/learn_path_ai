import streamlit as st
from typing import List, Dict

class ChatMemory:
    """
    Manages chat history
    Responsibilities:
    - Store chat history in memory
    - Provide methods to add and retrieve messages
    """
    def __init__(self, storage: List[Dict[str, str]]):
        """Initialize chat memory with storage"""
        self.storage = storage

    def load_history(self) -> List[Dict[str, str]]:
        """Load chat history from storage"""
        return self.storage

    def _add_message(self, role: str, content: str) -> Dict[str, str]:
        """Format and append a message to the chat history"""
        msg = {
            "role": role,
            "content": content
        }
        self.storage.append(msg)
        return msg
    
    def add_user_message(self, content: str):
        """Add a user message to the chat history"""
        self._add_message("user", content)
    
    def add_bot_message(self, content: str):
        """Add a bot message to the chat history"""
        self._add_message("assistant", content)

    def clean_history(self):
        """Clear the chat history"""
        self.storage.clear()