"""
messages.py

User-facing message keys and provider

Key features:
- MessageKey: enum of message keys
- MessageProvider: protocol for message provider
- DefaultMessageProvider: default implementation with templates
"""
from enum import Enum
from typing import Protocol

class MessageKey(str, Enum):
    """Keys for user-facing messages; use with MessageProvider.get or .format"""
    # Errors
    LLM_ERROR = "llm_error"
    LLM_STREAM_INTERRUPTED = "llm_stream_interrupted"
    UNEXPECTED_ERROR = "unexpected_error"

    # Validation
    EMPTY_INPUT = "empty_input"
    INPUT_TOO_LONG = "input_too_long"
    SESSION_EXPIRED = "session_expired"
    FILL_PROFILE = "fill_profile"

    # UI state
    THINKING = "thinking"

    # Profile
    PROFILE_ANALYZING = "profile_analyzing"
    PROFILE_EXTRACTED = "profile_extracted"

    # Roadmap
    ROADMAP_LOADING = "roadmap_loading"
    ROADMAP_CREATED = "roadmap_created"
    ROADMAP_ERROR = "roadmap_error"
    ROADMAP_INVALID_JSON = "roadmap_invalid_json"
    ROADMAP_INVALID_SCHEMA = "roadmap_invalid_schema"
    ROADMAP_GENERATION_FAILED = "roadmap_generation_failed"

class MessageProvider(Protocol):
    """Protocol for message provider"""
    def get(self, key: MessageKey) -> str:
        """Return message for key"""
        ...

    def format(self, key: MessageKey, **kwargs: str) -> str:
        """Return message formatted with kwargs (e.g. goal=..., max=...)"""
        ...

class DefaultMessageProvider:
    """
    Default message provider

    Responsibilities:
    - get(key): return template for MessageKey
    - format(key, **kwargs): substitute kwargs into template
    """

    _TEMPLATES: dict[MessageKey, str] = {
        MessageKey.LLM_ERROR: "Không thể kết nối hoặc tải tin nhắn. Vui lòng thử lại sau.",
        MessageKey.LLM_STREAM_INTERRUPTED: "\n\nKết nối bị gián đoạn. Câu trả lời phía trên chưa hoàn chỉnh. Vui lòng hỏi lại để nhận câu trả lời đầy đủ.*",
        MessageKey.UNEXPECTED_ERROR: "Đã xảy ra lỗi không mong muốn. Vui lòng thử lại sau.",

        MessageKey.EMPTY_INPUT: "Vui lòng nhập nội dung tin nhắn.",
        MessageKey.INPUT_TOO_LONG: "Tin nhắn quá dài. Vui lòng giới hạn trong {max} kí tự.",
        MessageKey.SESSION_EXPIRED: "Phiên làm việc đã hết hạn do không hoạt động. Vui lòng làm mới trang để tiếp tục.",
        MessageKey.FILL_PROFILE: (
            "Chưa đủ thông tin để tạo lộ trình Hãy cho biết mục tiêu học tập, trình độ và thời gian học tập "
            "(vd: Tôi muốn học Python từ đầu trong 3 tháng, mỗi ngày 1 giờ)."
        ),

        MessageKey.THINKING: "Đang suy nghĩ...",

        MessageKey.PROFILE_ANALYZING: "Đang phân tích thông tin...",
        MessageKey.PROFILE_EXTRACTED: "Đã trích xuất thông tin hồ sơ: mục tiêu {goal}, trình độ {level}, thời gian học {time}.",

        MessageKey.ROADMAP_LOADING: "Đang tạo lộ trình học tập...",
        MessageKey.ROADMAP_CREATED: "Lộ trình đã sẵn sàng. Bắt đầu học tập nào!",
        MessageKey.ROADMAP_ERROR: "Không thể tạo lộ trình. Vui lòng thử lại.",
        MessageKey.ROADMAP_INVALID_JSON: "Lộ trình nhận được không hợp lệ.",
        MessageKey.ROADMAP_INVALID_SCHEMA: "Lộ trình không đúng định dạng.",
        MessageKey.ROADMAP_GENERATION_FAILED: (
            "Không thể tạo lộ trình học tập sau nhiều lần thử. Vui lòng thử lại hoặc điều chỉnh thông tin học tập."
        ),
    }

    def get(self, key: MessageKey) -> str:
        return self._TEMPLATES.get(key, "")
    
    def format(self, key: MessageKey, **kwargs: str) -> str:
        template = self._TEMPLATES.get(key, "")
        return template.format(**kwargs) if kwargs else template
    
default_messages = DefaultMessageProvider()