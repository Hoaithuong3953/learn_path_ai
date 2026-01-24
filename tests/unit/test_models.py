"""
Unit tests for domain models
"""

import pytest
from datetime import datetime
from pydantic import ValidationError
from domain.models import (
    Resource,
    Milestone,
    Roadmap,
    UserProfile,
    ChatMessage
)

class TestResource:
    """Tests for Resource model"""
    def test_create_resource_minimal(self):
        """Test creating a valid resource with minimal fields"""
        resource = Resource(
            title="Python Tutorial",
            url="https://example.com/python",
            type="documentation"
        )

        assert resource.title == "Python Tutorial"
        assert str(resource.url) == "https://example.com/python"
        assert resource.type == "documentation"
        assert resource.description is None
        assert resource.difficulty is None

    def test_create_resource_full(self):
        """Test creating a resource with all fields"""
        resource = Resource(
            title="Python Crash Course",
            url="https://example.com/crash-course",
            type="video",
            description="Comprehensive Python tutorial",
            difficulty="beginner"
        )

        assert resource.description == "Comprehensive Python tutorial"
        assert resource.difficulty == "beginner"

    def test_resource_url_validation(self):
        """Test that url must be valid HttpUrl"""
        # Valid URL
        resource = Resource(
            title="Test",
            url="https://example.com",
            type="documentation"
        )

        assert str(resource.url) == "https://example.com/"

        # Invalid URL should raise ValidationError
        with pytest.raises(ValidationError):
            Resource(
                title="Test",
                url="not a url",
                type="documentation"
            )

    def test_resource_type_literal(self):
        """Test that resource type must be valid literal"""
        # Valid types
        valid_types = ["video", "article", "book", "course", "practice", "project", "documentation"]
        for resource_type in valid_types:
            resource = Resource(
                title="Test",
                url="https://example.com",
                type=resource_type
            )
            assert resource.type == resource_type

        # Invalid type should raise ValidationError
        with pytest.raises(Exception):
            Resource(
                title="Test",
                url="https://test.com",
                type="invalid_type"
            )

    def test_resource_difficulty_literal(self):
        """Test that difficulty must be valid literal if provided"""
        # Valid difficulties
        valid_difficulties = ["beginner", "intermediate", "advanced"]
        for difficulty in valid_difficulties:
            resource = Resource(
                title="Test",
                url="https://example.com",
                type="documentation",
                difficulty=difficulty
            )

            assert resource.difficulty == difficulty

        # Invalid difficulty should raise ValidationError
        with pytest.raises(ValidationError):
            Resource(
                title="Test",
                url="https://test.com",
                type="documentation",
                difficulty="invalid"
            )

    def test_resource_title_max_length(self):
        """Test that title max_length constraint is enforced"""
        # Valid length
        resource = Resource(
            title="A" * 200,
            url="https://example.com",
            type="documentation"
        )
        assert len(resource.title) == 200

        # Exceeds max_length should raise ValidationError
        with pytest.raises(ValidationError):
            Resource(
                title="A" * 201,
                url="https://example.com",
                type="documentation"
            )

class TestMilestone:
    """Tests for Milestone model"""

    def test_create_milestone_minimal(self):
        """Test creating a valid milestone with minimal fields"""
        milestone = Milestone(
            week=1,
            topic="Python Basics",
            description="Learn Python basics",
            resources=[
                Resource(
                    title="Tutorial",
                    url="https://example.com",
                    type="documentation"
                )
            ]
        )

        assert milestone.week == 1
        assert milestone.topic == "Python Basics"
        assert len(milestone.resources) == 1
        assert milestone.estimated_time is None
        assert milestone.learning_objectives is None

    def test_create_milestone_full(self):
        """Test creating a milestone with all fields"""
        milestone = Milestone(
            week=1,
            topic="Python Basics",
            description="Learn Python basics",
            resources=[
                Resource(
                    title="Tutorial",
                    url="https://example.com",
                    type="documentation"
                )
            ],
            estimated_time="5 giờ",
            learning_objectives=["Understand variables", "Learn functions"]
        )

        assert milestone.estimated_time == "5 giờ"
        assert len(milestone.learning_objectives) == 2

    def test_milestone_week_validation(self):
        """Test week must be >= 1"""
        # Valid week
        milestone = Milestone(
            week=1,
            topic="Test",
            description="Test description",
            resources=[
                Resource(
                    title="Test resource",
                    url="https://example.com",
                    type="documentation"
                )
            ]
        )

        assert milestone.week == 1

        # Week < 1 should raise ValidationError
        with pytest.raises(ValidationError):
            Milestone(
                week=0,
                topic="Test",
                description="Test",
                resources=[
                    Resource(
                        title="Test resource",
                        url="https://example.com",
                        type="documentation"
                    )
                ]
            )

    def test_milestone_resources_min_length(self):
        """Test that resources list must be have at least 1 item"""
        # Valid: 1 resource
        milestone = Milestone(
            week=1,
            topic="Test",
            description="Test",
            resources=[
                Resource(
                    title="Test resource",
                    url="https://example.com",
                    type="documentation"
                )
            ]
        )
        assert len(milestone.resources) == 1

        # Empty resource list should raise ValidationError
        with pytest.raises(ValidationError):
            Milestone(
                week=1,
                topic="Test",
                description="Test",
                resources=[]
            )

    def test_milestone_topic_max_length(self):
        """Test that topic max_length constraint is enforced"""
        # Valid length
        milestone = Milestone(
            week=1,
            topic="a" * 200,
            description="Test",
            resources=[
                Resource(
                    title="Test",
                    url="https://example.com",
                    type="documentation"
                )
            ]
        )
        assert len(milestone.topic) == 200

        # Exceeds max_length should raise ValidationError
        with pytest.raises(ValidationError):
            Milestone(
                week=1,
                topic="a"*201,
                description="Test",
                resources=[
                    Resource(
                        title="Test",
                        url="https://example.com",
                        type="documentation"
                    )
                ]
            )

    def test_milestone_description_max_length(self):
        """Test that description max_length_constraint is enforced"""
        # Valid length
        milestone = Milestone(
            week=1,
            topic="Test",
            description="a"*1000,
            resources=[
                Resource(
                    title="Test",
                    url="https://example.com",
                    type="documentation"
                )
            ]
        )
        assert len(milestone.description) == 1000

        # Exceeds max_length should raise ValidationError
        with pytest.raises(ValidationError):
            Milestone(
                week=1,
                topic="Test",
                description="a"*1001,
                resources=[
                    Resource(
                        title="Test",
                        url="https://example.com",
                        type="documentation"
                    )
                ]
            )
