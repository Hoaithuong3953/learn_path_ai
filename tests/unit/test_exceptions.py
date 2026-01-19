"""
Unit tests for LearnPath exceptions
"""
import pytest
from http import HTTPStatus

from utils.exceptions import (
    LearnPathException,
    LLMServiceError,
    ValidationError
)

class TestLearnPathException:
    """
    Test base LearnPathException class
    """

    def test_exception_creation_with_defaults(self):
        """Test exception creation with default values"""
        exc = LearnPathException()

        assert exc.code == "GENERAL_ERROR"
        assert exc.message == "An unexpected error occurred"
        assert exc.status_code == HTTPStatus.INTERNAL_SERVER_ERROR.value
        assert exc.extra == {}

    def test_exception_creation_with_custom_values(self):
        """Test exception creation with custom values"""
        exc = LearnPathException(
            message="Custom error message",
            code="CUSTOM_ERROR",
            status_code=400,
            extra_field="extra_value"
        )

        assert exc.code == "CUSTOM_ERROR"
        assert exc.message == "Custom error message"
        assert exc.status_code == 400
        assert exc.extra == {"extra_field": "extra_value"}

    def test_to_dict_method(self):
        """Test to_dict() method converts exception to dictionary"""
        exc = LearnPathException(
            message="Test error",
            code="TEST_ERROR",
            status_code=400,
            user_id="user123"
        )

        result = exc.to_dict()

        assert "error" in result
        assert result["error"]["code"] == "TEST_ERROR"
        assert result["error"]["message"] == "Test error"
        assert result["error"]["status_code"] == 400
        assert result["error"]["user_id"] == "user123"

    def test_to_dict_return_type(self):
        """Test that to_dict() returns Dict[str, Any] type"""
        exc = LearnPathException()
        result = exc.to_dict()

        assert isinstance(result, dict)
        assert isinstance(result["error"], dict)

    def test__str__method(self):
        """Test __str__ method for user-friendly error messages"""
        exc = LearnPathException(
            message="Test error",
            code="TEST_ERROR",
            status_code=400
        )

        str_repr = str(exc)

        assert "TEST_ERROR" in str_repr
        assert "400" in str_repr
        assert "Test error" in str_repr
