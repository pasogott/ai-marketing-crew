"""Tests for Crew initialization and configuration"""
import pytest
from ai_marketing_crew.crew import AiMarketingCrew


class TestCrewInitialization:
    """Test crew initialization and setup"""

    def test_crew_class_exists(self):
        """Test that AiMarketingCrew class exists and is properly decorated"""
        assert hasattr(AiMarketingCrew, 'crew')
        assert hasattr(AiMarketingCrew, 'head_of_marketing')
        assert hasattr(AiMarketingCrew, 'content_creator_social')
        assert hasattr(AiMarketingCrew, 'content_writer_blog')
        assert hasattr(AiMarketingCrew, 'seo_specialist')

    def test_all_tasks_are_defined(self):
        """Test that all required tasks are defined"""
        # Check that task methods exist without instantiating
        assert hasattr(AiMarketingCrew, 'market_research_task')
        assert hasattr(AiMarketingCrew, 'build_marketing_strategy_task')
        assert hasattr(AiMarketingCrew, 'build_content_calendar_task')
        assert hasattr(AiMarketingCrew, 'generate_social_posts_task')
        assert hasattr(AiMarketingCrew, 'generate_blog_draft_task')
        assert hasattr(AiMarketingCrew, 'generate_seo_keywords_task')

    def test_tool_initialization_method_exists(self):
        """Test that tool initialization method exists"""
        assert hasattr(AiMarketingCrew, '_init_tools')

