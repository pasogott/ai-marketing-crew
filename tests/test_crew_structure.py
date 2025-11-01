"""Tests for crew structure and configuration"""
import pytest
import inspect
from crewai import Process
from ai_marketing_crew.crew import AiMarketingCrew


class TestCrewStructure:
    """Test crew structure, agents, and tasks"""

    def test_crew_method_signature(self):
        """Test that crew method exists and is callable"""
        assert hasattr(AiMarketingCrew, 'crew')
        crew_method = getattr(AiMarketingCrew, 'crew')
        # CrewBase decorator wraps methods, so we just check it's callable
        assert callable(crew_method)

    def test_all_agent_methods_exist(self):
        """Test that all agent methods exist"""
        agent_methods = [
            'head_of_marketing',
            'content_creator_social',
            'content_writer_blog',
            'seo_specialist'
        ]
        
        for method_name in agent_methods:
            assert hasattr(AiMarketingCrew, method_name), f"Agent method '{method_name}' missing"
            method = getattr(AiMarketingCrew, method_name)
            assert callable(method), f"'{method_name}' is not callable"

    def test_all_task_methods_exist(self):
        """Test that all task methods exist"""
        task_methods = [
            'market_research_task',
            'build_marketing_strategy_task',
            'build_content_calendar_task',
            'generate_social_posts_task',
            'generate_blog_draft_task',
            'generate_seo_keywords_task'
        ]
        
        for method_name in task_methods:
            assert hasattr(AiMarketingCrew, method_name), f"Task method '{method_name}' missing"
            method = getattr(AiMarketingCrew, method_name)
            assert callable(method), f"'{method_name}' is not callable"
