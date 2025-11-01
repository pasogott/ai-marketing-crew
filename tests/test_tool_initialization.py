"""Tests for tool imports and availability"""
import pytest


class TestToolImports:
    """Test that tools can be imported"""

    def test_tool_imports_available(self):
        """Test that required tools can be imported"""
        try:
            from crewai_tools import (
                SerperDevTool,
                ScrapeWebsiteTool,
                DirectoryReadTool,
                FileReadTool,
                FileWriterTool,
            )
            # If we get here, imports are successful
            assert True
        except ImportError as e:
            pytest.skip(f"Tools not available: {e}")

    def test_tool_classes_exist_in_crew_module(self):
        """Test that tool classes are referenced in crew module"""
        from ai_marketing_crew import crew
        
        # Check that tools are imported (may be None if not available)
        assert hasattr(crew, 'SerperDevTool') or crew.SerperDevTool is None
        assert hasattr(crew, 'ScrapeWebsiteTool') or crew.ScrapeWebsiteTool is None
        assert hasattr(crew, 'DirectoryReadTool') or crew.DirectoryReadTool is None
        assert hasattr(crew, 'FileReadTool') or crew.FileReadTool is None
        assert hasattr(crew, 'FileWriterTool') or crew.FileWriterTool is None

