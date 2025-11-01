"""Integration tests for crew execution"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from ai_marketing_crew.crew import AiMarketingCrew


class TestCrewExecution:
    """Integration tests for crew execution flow"""

    @pytest.mark.integration
    @pytest.mark.slow
    @patch('crewai_tools.SerperDevTool')
    @patch('crewai_tools.ScrapeWebsiteTool')
    @patch('crewai_tools.DirectoryReadTool')
    @patch('crewai_tools.FileReadTool')
    @patch('crewai_tools.FileWriterTool')
    @patch('crewai.Crew.kickoff')
    def test_crew_can_be_initialized_for_execution(self, mock_kickoff, mock_file_write,
                                                     mock_file_read, mock_dir_read,
                                                     mock_scrape, mock_serper, mock_env_vars,
                                                     sample_inputs):
        """Test that crew can be initialized and prepared for execution"""
        # Mock kickoff to return a simple result
        mock_kickoff.return_value = Mock()
        mock_kickoff.return_value.raw = "Test execution result"
        
        crew_instance = AiMarketingCrew()
        crew = crew_instance.crew()
        
        # Crew should be initialized
        assert crew is not None
        assert len(crew.agents) == 4
        assert len(crew.tasks) == 6

    @pytest.mark.integration
    def test_resources_directory_creation(self, tmp_path, mock_env_vars):
        """Test that resources directory is created"""
        import os
        from pathlib import Path
        
        # Change to tmp directory
        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            # Import here to use the tmp_path
            with patch('ai_marketing_crew.crew.SerperDevTool'):
                with patch('ai_marketing_crew.crew.ScrapeWebsiteTool'):
                    with patch('ai_marketing_crew.crew.DirectoryReadTool'):
                        with patch('ai_marketing_crew.crew.FileReadTool'):
                            with patch('ai_marketing_crew.crew.FileWriteTool'):
                                # Import after changing directory
                                from ai_marketing_crew.crew import resources_dir, drafts_dir
                                
                                # Resources directory should be created
                                assert resources_dir.exists()
                                assert drafts_dir.exists()
        finally:
            os.chdir(original_cwd)

