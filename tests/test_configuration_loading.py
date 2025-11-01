"""Tests for YAML configuration loading"""
import pytest
from pathlib import Path
from ai_marketing_crew.crew import AiMarketingCrew


class TestConfigurationLoading:
    """Test loading of YAML configurations"""

    def test_agents_config_exists(self, mock_env_vars):
        """Test that agents configuration is loaded"""
        with patch('crewai_tools.SerperDevTool'):
            with patch('crewai_tools.ScrapeWebsiteTool'):
                with patch('crewai_tools.DirectoryReadTool'):
                    with patch('crewai_tools.FileReadTool'):
                        with patch('crewai_tools.FileWriteTool'):
                            crew = AiMarketingCrew()
                            
                            # CrewBase should load agents_config
                            assert hasattr(crew, 'agents_config')
                            assert crew.agents_config is not None

    def test_tasks_config_exists(self, mock_env_vars):
        """Test that tasks configuration is loaded"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew = AiMarketingCrew()
                            
                            # CrewBase should load tasks_config
                            assert hasattr(crew, 'tasks_config')
                            assert crew.tasks_config is not None

    def test_agents_yaml_has_required_agents(self, mock_env_vars):
        """Test that agents.yaml contains all required agents"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew = AiMarketingCrew()
                            
                            required_agents = [
                                'head_of_marketing',
                                'content_creator_social',
                                'content_writer_blog',
                                'seo_specialist'
                            ]
                            
                            for agent_name in required_agents:
                                assert agent_name in crew.agents_config

    def test_tasks_yaml_has_required_tasks(self, mock_env_vars):
        """Test that tasks.yaml contains all required tasks"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew = AiMarketingCrew()
                            
                            required_tasks = [
                                'market_research_task',
                                'build_marketing_strategy_task',
                                'build_content_calendar_task',
                                'generate_social_posts_task',
                                'generate_blog_draft_task',
                                'generate_seo_keywords_task'
                            ]
                            
                            for task_name in required_tasks:
                                assert task_name in crew.tasks_config

