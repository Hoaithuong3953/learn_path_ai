from typing import Generator

from utils.logger import logger
from utils.exceptions import LLMServiceError
from ai.llm_client import GeminiClient
from memory.chat_memory import ChatMemory
from config.constant import CHAT_ERROR_MESSAGES

class ChatService:
    """
    Service Layer for Chat Operations.
    Responsibility: Isolate the UI from the complexity of managing AI state and API calls.
    """
    def __init__(self, ai_client: GeminiClient, memory: ChatMemory):
        self.ai = ai_client
        self.memory = memory

    def process_message(self, user_input: str) -> Generator[str, None, None]:
        """
        Processing a user's chat message.
        """
        if not user_input or not user_input.strip():
            logger.warning("Empty user input received in ChatService")
            yield "Vui lòng nhập nội dung tin nhắn."
            return

        self.memory.add_user_message(user_input)

        yield from self._stream_response(user_input)

    def _handle_stream_error(self, error: Exception, error_type: str) -> str:
        """
        Helper method to handle streaming errors consistently.
        """
        if error_type == "llm_service":
            logger.error(f"AI Service error: {error}")
            return "\n\n[Lỗi kết nối: Không thể tải toàn bộ tin nhắn, vui lòng thử lại]"
        else:
            logger.error(f"Unexpected Chat Error: {error}")
            return "\n\n[Lỗi hệ thống: Đã xảy ra sự cố không mong muốn]"

    def _stream_response(self, user_input: str) -> Generator[str, None, None]:
        """
        Handles the LLM streaming lifecycle.
        """
        raw_history = self.memory.load_history()
        history_context = raw_history[:-1]

        logger.info(f"Processing chat. Context length: {len(history_context)}")

        full_response = ""
        error_occurred = False

        try:
            stream_generation = self.ai.stream_chat(
                history=history_context,
                new_message=user_input   
            )

            for chunk in stream_generation:
                full_response += chunk
                yield chunk

        except LLMServiceError as e:
            error_message = self._handle_stream_error(e, "llm_service")
            full_response += error_message
            yield error_message
            error_occurred = True

        except Exception as e:
            error_message = self._handle_stream_error(e, "unexpected")
            full_response += error_message
            yield error_message
            error_occurred = True

        finally:
            if full_response:
                self.memory.add_bot_message(full_response)
                logger.info(f"Saved bot response (Length: {len(full_response)}), Error: {error_occurred}")