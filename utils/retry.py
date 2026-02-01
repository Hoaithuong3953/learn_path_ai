"""
retry.py

Retry helpers for external API calls (Gemini transient errors)

Key features:
- gemini_retry: decorator for transient Gemini errors (exponential backoff)
- TRANSIENT_ERRORS: tuple of retryable Google API exceptions
"""

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type, before_sleep_log
from google.api_core import exceptions as google_exceptions

from utils.logger import logger

TRANSIENT_ERRORS = (
    google_exceptions.DeadlineExceeded,
    google_exceptions.ResourceExhausted,
    google_exceptions.ServiceUnavailable,
    google_exceptions.Aborted
)

def gemini_retry(max_retries: int = 3):
    """
    Build a tenacity retry decorator for transient Gemini API errors

    Args:
        max_retries: Maximum number of retry attempts before failing

    Returns:
        Decorator that retries on TRANSIENT_ERRORS with exponential backoff
    """
    return retry(
        reraise=True,
        stop=stop_after_attempt(max_retries),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type(TRANSIENT_ERRORS),
        before_sleep=before_sleep_log(logger, "warning")
    )