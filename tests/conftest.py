"""Pytest configuration and shared fixtures"""
import pytest


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
def sample_inputs():
    """Sample inputs for testing"""
    return {
        'product_name': 'Test Product',
        'product_description': 'A test product for testing purposes',
        'target_audience': 'Test users',
        'budget': '€10.000',
        'current_date': '2024-01-01',
    }

