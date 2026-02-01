"""
llm_client.py

Protocol definition for LLM client implementations (Gemini, OpenAI, etc.)

Key features:
- generate_text: single prompt → full response
- stream_chat: history + new message → streaming chunks
"""

from typing import Protocol, List, Generator
from domain import ChatMessage

class LLMClient(Protocol):
    """
    Interface for LLM clients (Gemini, OpenAI, etc.)

    Responsibilities:
    - generate_text: non-streaming completion from a prompt
    - stream_chat: streaming completion with conversation history
    """

    def generate_text(self, prompt: str) -> str:
        """
        Generate text from a single prompt.

        Args:
            prompt: Input text for the model

        Returns:
            Full response text from the model
        """
        ...

    def stream_chat(self, history: List[ChatMessage], new_message: str) -> Generator[str, None, None]:
        """
        Stream chat response given history and new user message.

        Args:
            history: Previous messages in the conversation
            new_message: Latest user message

        Yields:
            Chunks of the model response as they arrive
        """
        ...