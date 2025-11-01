"""Tests for YAML configuration loading"""
import pytest
import yaml
from pathlib import Path


class TestConfigurationLoading:
    """Test loading of YAML configurations"""

    def test_agents_yaml_file_exists(self):
        """Test that agents.yaml file exists and is valid YAML"""
        agents_yaml = Path("src/ai_marketing_crew/config/agents.yaml")
        assert agents_yaml.exists(), "agents.yaml file not found"
        
        with open(agents_yaml) as f:
            config = yaml.safe_load(f)
            assert config is not None, "agents.yaml is empty or invalid"

    def test_tasks_yaml_file_exists(self):
        """Test that tasks.yaml file exists and is valid YAML"""
        tasks_yaml = Path("src/ai_marketing_crew/config/tasks.yaml")
        assert tasks_yaml.exists(), "tasks.yaml file not found"
        
        with open(tasks_yaml) as f:
            config = yaml.safe_load(f)
            assert config is not None, "tasks.yaml is empty or invalid"

    def test_agents_yaml_has_required_agents(self):
        """Test that agents.yaml contains all required agents"""
        agents_yaml = Path("src/ai_marketing_crew/config/agents.yaml")
        
        with open(agents_yaml) as f:
            config = yaml.safe_load(f)
            
            required_agents = [
                'head_of_marketing',
                'content_creator_social',
                'content_writer_blog',
                'seo_specialist'
            ]
            
            for agent_name in required_agents:
                assert agent_name in config, f"Agent '{agent_name}' not found in agents.yaml"
                assert 'role' in config[agent_name], f"Agent '{agent_name}' missing 'role'"
                assert 'goal' in config[agent_name], f"Agent '{agent_name}' missing 'goal'"

    def test_tasks_yaml_has_required_tasks(self):
        """Test that tasks.yaml contains all required tasks"""
        tasks_yaml = Path("src/ai_marketing_crew/config/tasks.yaml")
        
        with open(tasks_yaml) as f:
            config = yaml.safe_load(f)
            
            required_tasks = [
                'market_research_task',
                'build_marketing_strategy_task',
                'build_content_calendar_task',
                'generate_social_posts_task',
                'generate_blog_draft_task',
                'generate_seo_keywords_task'
            ]
            
            for task_name in required_tasks:
                assert task_name in config, f"Task '{task_name}' not found in tasks.yaml"
                assert 'description' in config[task_name], f"Task '{task_name}' missing 'description'"
                assert 'expected_output' in config[task_name], f"Task '{task_name}' missing 'expected_output'"

