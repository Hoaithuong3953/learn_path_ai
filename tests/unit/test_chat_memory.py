"""
test_chat_memory.py

Unit tests for ChatMemory (in-memory history storage)

Key features:
- Initial empty history, add_message, add_user_message, add_bot_message, clean_history
"""
from datetime import datetime

from domain import ChatMessage
from memory import ChatMemory

class TestChatMemory:
    """Tests for ChatMemory (in-memory history storage)"""

    def test_initial_empty_history(self):
        """New ChatMemory with empty storage has no messages"""
        memory = ChatMemory(storage=[])

        history = memory.load_history()

        assert history == []

    def test_add_message_appends_to_history(self):
        """add_message appends ChatMessage to internal storage"""
        memory = ChatMemory(storage=[])
        msg = ChatMessage(role="user", content="Hello")

        memory.add_message(msg)

        history = memory.load_history()
        assert len(history) == 1

    def test_add_user_message_creates_user_chat_message(self):
        """add_user_message creates a ChatMessage with role='user'"""
        memory = ChatMemory(storage=[])
        memory.add_user_message("Hi")

        history = memory.load_history()
        assert len(history) == 1
        
        message = history[0]
        assert message.role == "user"
        assert message.content == "Hi"
        assert isinstance(message.timestamp, datetime)

    def test_add_bot_message_creates_assistant_chat_message(self):
        """add_bot_message creates a ChatMessage with role='assistant'"""
        memory = ChatMemory(storage=[])
        memory.add_bot_message("Hi, I'm LearnPath AI")

        history = memory.load_history()
        assert len(history) == 1
        
        message = history[0]
        assert message.role == "assistant"
        assert message.content == "Hi, I'm LearnPath AI"
        assert isinstance(message.timestamp, datetime)

    def test_clean_history_clears_all_messages(self):
        """clean_history removes all stored messages"""
        memory = ChatMemory(storage=[])
        memory.add_user_message("msg1")
        memory.add_bot_message("msg2")

        history = memory.load_history()
        assert len(history) == 2

        memory.clean_history()
        assert len(history) == 0