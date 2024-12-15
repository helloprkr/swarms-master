"""Basic tests for Swarms."""
import pytest
from swarms import Agent, OpenAIChat

def test_agent_initialization():
    """Test basic agent initialization."""
    agent = Agent(
        agent_name="TestAgent",
        system_prompt="Test prompt",
    )
    assert agent.agent_name == "TestAgent"
    assert agent.system_prompt == "Test prompt"

def test_agent_run():
    """Test basic agent run."""
    agent = Agent()
    result = agent.run("Test task")
    assert isinstance(result, str)
    assert "Test task" in result 