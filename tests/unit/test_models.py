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

class TestRoadmap:
    """Tests for Roadmap model"""

    def test_create_roadmap_minimal(self):
        """Test creating a valid roadmap with minimal fields"""
        roadmap = Roadmap(
            topic="Learn Python",
            duration_week=1,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
            ]
        )

        assert roadmap.topic == "Learn Python"
        assert roadmap.duration_week == 1
        assert roadmap.description is None
        assert roadmap.prerequisites is None
        assert isinstance(roadmap.created_at, datetime)

    def test_create_roadmap_full(self):
        """Test creating roadmap with all fields"""
        roadmap = Roadmap(
            topic="Learn Python",
            title="Python Learning Path",
            description="Complete Python roadmap",
            duration_week=2,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
                Milestone(week=2, topic="W2", description="D2", resources=[
                    Resource(title="R2", url="https://example.com/2", type="documentation")
                ]),
            ],
            prerequisites=["Basic programming knowledge"]
        )

        assert roadmap.title == "Python Learning Path"
        assert roadmap.description == "Complete Python roadmap"
        assert len(roadmap.prerequisites) == 1

    def test_roadmap_auto_set_title(self):
        """Test that title is auto-set to topic if not provided"""
        # Title not provided
        roadmap = Roadmap(
            topic="Learn Python",
            duration_week=1,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
            ]
        )
        assert roadmap.title == "Learn Python"

        # Title provided
        roadmap2 = Roadmap(
            topic="Learn Python",
            title="Custom title",
            duration_week=1,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
            ]
        )
        assert roadmap2.title == "Custom title"

    def test_roadmap_sequential_weeks(self):
        """Test that weeks must be sequential starting from 1"""
        # Valid: Sequential weeks
        roadmap = Roadmap(
            topic="Test",
            duration_week=3,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
                Milestone(week=2, topic="W2", description="D2", resources=[
                    Resource(title="R2", url="https://example.com/2", type="documentation")
                ]),
                Milestone(week=3, topic="W3", description="D3", resources=[
                    Resource(title="R3", url="https://example.com/3", type="documentation")
                ])
            ]
        )
        assert len(roadmap.milestones) == 3

        # Invalid: Non-sequential weeks
        with pytest.raises(ValidationError) as exc_info:
            Roadmap(
                topic="Test",
                duration_week=3,
                milestones=[
                    Milestone(week=1, topic="W1", description="D1", resources=[
                        Resource(title="R1", url="https://example.com/1", type="documentation")
                    ]),
                    Milestone(week=3, topic="W3", description="D3", resources=[
                        Resource(title="R3", url="https://example.com/3", type="documentation")
                    ])
                ]
            )
        assert "sequential" in str(exc_info.value).lower()

        # Invalid: Starting from wrong number
        with pytest.raises(ValidationError):
            Roadmap(
                topic="Test",
                duration_week=2,
                milestones=[
                    Milestone(week=2, topic="W2", description="D2", resources=[
                        Resource(title="R2", url="https://example.com/2", type="documentation")
                    ]),
                    Milestone(week=3, topic="W3", description="D3", resources=[
                        Resource(title="R3", url="https://example.com/3", type="documentation")
                    ])
                ]
            )
    
    def test_roadmap_milestone_count_matches_duration(self):
        """Test that number of milestones must match duration_week"""
        # Valid: Count matches
        roadmap = Roadmap(
            topic="Test",
            duration_week=3,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
                Milestone(week=2, topic="W2", description="D2", resources=[
                    Resource(title="R2", url="https://example.com/2", type="documentation")
                ]),
                Milestone(week=3, topic="W3", description="D3", resources=[
                    Resource(title="R3", url="https://example.com/3", type="documentation")
                ])
            ]
        )
        assert len(roadmap.milestones) == roadmap.duration_week

        # Invalid: Count doesn't match
        with pytest.raises(ValidationError) as exc_info:
            Roadmap(
                topic="Test",
                duration_week=2,
                milestones=[
                    Milestone(week=1, topic="W1", description="D1", resources=[
                        Resource(title="R1", url="https://example.com/1", type="documentation")
                    ]),
                    Milestone(week=2, topic="W2", description="D2", resources=[
                        Resource(title="R2", url="https://example.com/2", type="documentation")
                    ]),
                    Milestone(week=3, topic="W3", description="D3", resources=[
                        Resource(title="R3", url="https://example.com/3", type="documentation")
                    ])
                ]
            )
        assert "must match duration_week" in str(exc_info.value)

    def test_roadmap_duration_week_validation(self):
        """Test that duration_week must be >= 1"""
        # Valid duration
        roadmap = Roadmap(
            topic="Test",
            duration_week=1,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
            ]
        )
        assert roadmap.duration_week == 1

        # Invalid: duration_week < 1
        with pytest.raises(ValidationError):
            Roadmap(
                topic="Test",
                duration_week=0,
                milestones=[
                    Milestone(week=1, topic="W1", description="D1", resources=[
                        Resource(title="R1", url="https://example.com/1", type="documentation")
                    ]),
                ]
            )

    def test_roadmap_milestones_min_length(self):
        """Test that milestones list must be have at least 1 item"""
        # Valid: 1 milestone
        roadmap = Roadmap(
            topic="Test",
            duration_week=1,
            milestones=[
                Milestone(week=1, topic="W1", description="D1", resources=[
                    Resource(title="R1", url="https://example.com/1", type="documentation")
                ]),
            ]
        )
        assert len(roadmap.milestones) == 1

        # Invalid: Empty milestones
        with pytest.raises(ValidationError):
            Roadmap(
                topic="Test",
                duration_week=1,
                milestones=[]
            )

class TestUserProfile:
    """Test for UserProfile model"""
    def test_create_user_profile_minimal(self):
        profile = UserProfile(
            goal="Learn Python",
            current_level="beginner",
            time_commitment="2 giờ/ngày"
        )
        assert profile.goal == "Learn Python"
        assert profile.current_level == "beginner"
        assert profile.time_commitment == "2 giờ/ngày"
        assert profile.learning_style is None
        assert profile.background is None
        assert profile.constraints is None

    def test_create_user_profile_full(self):
        """Test creating user profile with all fields"""
        profile = UserProfile(
            goal="Learn Python",
            current_level="intermedia",
            time_commitment="10 hours/week",
            learning_style="Visual",
            background="Software engineer",
            constraints=["Free only", "Weekends only"]
        )
        assert profile.learning_style == "Visual"
        assert profile.background == "Software engineer"
        assert len(profile.constraints) == 2

    def test_user_profile_goal_max_length(self):
        """Test that goal max_length constraint is enforced"""
        # Valid length
        profile = UserProfile(
            goal="A"*500,
            current_level="beginner",
            time_commitment="2 hours/day"
        )
        assert len(profile.goal) == 500

        # Exceeds max_length should raise ValidationError
        with pytest.raises(ValidationError):
            UserProfile(
                goal="A"*501,
                current_level="beginner",
                time_commitment="2 hours/day"
            )

class TestChatMessage:
    """Tests for ChatMessage model"""
    def test_create_chat_message_user(self):
        """Test creating a user chat message"""
        message = ChatMessage(
            role="user",
            content="Hello"
        )
        assert message.role == "user"
        assert message.content == "Hello"
        assert isinstance(message.timestamp, datetime)

    def test_create_chat_message_assistant(self):
        """Test creating an assistant chat message"""
        message = ChatMessage(
            role="assistant",
            content="Hello"
        )
        assert message.role == "assistant"
        assert message.content == "Hello"
        assert isinstance(message.timestamp, datetime)

    def test_create_chat_message_system(self):
        """Test creating a system chat message"""
        message = ChatMessage(
            role="user",
            content="System error"
        )
        assert message.role == "user"
        assert message.content == "System error"
        assert isinstance(message.timestamp, datetime)

    def test_chat_message_role_literal(self):
        """Test that role must be valid literal"""
        # Valid roles
        valid_roles = ["system", "user", "assistant"]
        for role in valid_roles:
            message = ChatMessage(role=role, content="Test")
            assert message.role == role

        # Invalid role should raise ValidationError
        with pytest.raises(ValidationError):
            ChatMessage(
                role="invalid_role",
                content="Test"
            )