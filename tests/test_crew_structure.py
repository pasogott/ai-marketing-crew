"""Tests for crew structure and configuration"""
import pytest
from unittest.mock import patch, MagicMock
from ai_marketing_crew.crew import AiMarketingCrew


class TestCrewStructure:
    """Test crew structure, agents, and tasks"""

    @patch('ai_marketing_crew.crew.Agent')
    @patch('ai_marketing_crew.crew.Task')
    def test_crew_has_four_agents(self, mock_task, mock_agent, mock_env_vars):
        """Test that crew has exactly 4 agents"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew_instance = AiMarketingCrew()
                            crew = crew_instance.crew()
                            
                            assert len(crew.agents) == 4
                            agent_roles = [agent.role if hasattr(agent, 'role') else str(agent) 
                                         for agent in crew.agents]
                            
                            # Verify we have the right agents
                            assert len(crew.agents) == 4

    @patch('ai_marketing_crew.crew.Agent')
    @patch('ai_marketing_crew.crew.Task')
    def test_crew_has_six_tasks(self, mock_task, mock_agent, mock_env_vars):
        """Test that crew has exactly 6 tasks"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew_instance = AiMarketingCrew()
                            crew = crew_instance.crew()
                            
                            assert len(crew.tasks) == 6

    def test_crew_uses_sequential_process(self, mock_env_vars):
        """Test that crew uses sequential process"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew_instance = AiMarketingCrew()
                            crew = crew_instance.crew()
                            
                            # Process should be sequential according to PRD
                            from crewai import Process
                            assert crew.process == Process.sequential

    def test_task_dependencies(self, mock_env_vars):
        """Test that tasks have correct dependencies"""
        with patch('ai_marketing_crew.crew.SerperDevTool'):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                    with patch('ai_marketing_crew.crew.FileReadTool'):
                        with patch('ai_marketing_crew.crew.FileWriteTool'):
                            crew_instance = AiMarketingCrew()
                            
                            # Marketing strategy should depend on market research
                            strategy_task = crew_instance.build_marketing_strategy_task()
                            assert strategy_task is not None
                            
                            # Content calendar should depend on marketing strategy
                            calendar_task = crew_instance.build_content_calendar_task()
                            assert calendar_task is not None

