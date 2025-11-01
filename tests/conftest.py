"""Pytest configuration and shared fixtures"""
import os
import pytest
from unittest.mock import Mock, patch
from pathlib import Path


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing"""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("SERPER_API_KEY", "test-serper-key")
    yield
    # Cleanup
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("SERPER_API_KEY", raising=False)


@pytest.fixture
def mock_env_vars_no_serper(monkeypatch):
    """Mock environment variables without Serper key"""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    yield
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("SERPER_API_KEY", raising=False)


@pytest.fixture
def resources_dir(tmp_path):
    """Create a temporary resources directory for testing"""
    resources = tmp_path / "resources"
    drafts = resources / "drafts"
    resources.mkdir()
    drafts.mkdir()
    return resources


@pytest.fixture
def sample_inputs():
    """Sample inputs for testing"""
    return {
        'product_name': 'Test Product',
        'product_description': 'A test product for testing purposes',
        'target_audience': 'Test users',
        'budget': '€10.000',
        'current_date': '2024-01-01',
    }

