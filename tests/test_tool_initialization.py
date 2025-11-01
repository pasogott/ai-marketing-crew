"""Tests for tool initialization and error handling"""
import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from ai_marketing_crew.crew import AiMarketingCrew


class TestToolInitialization:
    """Test tool initialization with various configurations"""

    def test_tool_init_with_serper_key(self, mock_env_vars):
        """Test tool initialization when Serper API key is present"""
        with patch('ai_marketing_crew.crew.SerperDevTool') as mock_serper:
            mock_serper.return_value = Mock()
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool') as mock_scrape:
                mock_scrape.return_value = Mock()
                with patch('ai_marketing_crew.crew.DirectoryReadTool') as mock_dir:
                    mock_dir.return_value = Mock()
                    with patch('ai_marketing_crew.crew.FileReadTool') as mock_file_read:
                        mock_file_read.return_value = Mock()
                        with patch('ai_marketing_crew.crew.FileWriteTool') as mock_file_write:
                            mock_file_write.return_value = Mock()
                            
                            crew = AiMarketingCrew()
                            
                            # SerperDevTool should be initialized
                            assert 'serper_dev_tool' in crew.tools

    def test_tool_init_without_serper_key(self, mock_env_vars_no_serper):
        """Test tool initialization when Serper API key is missing"""
        with patch('ai_marketing_crew.crew.SerperDevTool') as mock_serper:
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool') as mock_scrape:
                mock_scrape.return_value = Mock()
                with patch('ai_marketing_crew.crew.DirectoryReadTool') as mock_dir:
                    mock_dir.return_value = Mock()
                    with patch('ai_marketing_crew.crew.FileReadTool') as mock_file_read:
                        mock_file_read.return_value = Mock()
                        with patch('ai_marketing_crew.crew.FileWriteTool') as mock_file_write:
                            mock_file_write.return_value = Mock()
                            
                            crew = AiMarketingCrew()
                            
                            # Crew should still initialize without Serper
                            assert crew is not None
                            # SerperDevTool should not be in tools
                            assert 'serper_dev_tool' not in crew.tools

    def test_tool_init_handles_exceptions(self, mock_env_vars):
        """Test that tool initialization handles exceptions gracefully"""
        with patch('ai_marketing_crew.crew.SerperDevTool', side_effect=Exception("Tool error")):
            with patch('ai_marketing_crew.crew.ScrapeWebsiteTool', side_effect=Exception("Tool error")):
                with patch('ai_marketing_crew.crew.DirectoryReadTool', side_effect=Exception("Tool error")):
                    with patch('ai_marketing_crew.crew.FileReadTool', side_effect=Exception("Tool error")):
                        with patch('ai_marketing_crew.crew.FileWriteTool', side_effect=Exception("Tool error")):
                            # Should not raise exception, but handle it gracefully
                            crew = AiMarketingCrew()
                            assert crew is not None
                            # Tools dict should exist even if empty
                            assert hasattr(crew, 'tools')

