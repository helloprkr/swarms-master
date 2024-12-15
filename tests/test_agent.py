import unittest
from swarms import Agent


class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent(
            agent_name="TestAgent",
            system_prompt="This is a test agent.",
            llm=None,  # Mock or stub the LLM for testing
            max_loops=1,
            autosave=False,
            verbose=False,
            dynamic_temperature_enabled=False,
            saved_state_path="test_agent.json",
            user_name="test_user",
            retry_attempts=1,
            context_length=200000,
            return_step_meta=False,
            output_type="string",
        )

    def test_agent_initialization(self):
        self.assertEqual(self.agent.agent_name, "TestAgent")
        self.assertEqual(self.agent.max_loops, 1)
        self.assertFalse(self.agent.autosave)

    def test_agent_run(self):
        # Mock the run method to test its behavior
        result = self.agent.run("Test task")
        self.assertIsNotNone(result)  # Check that the result is not None


if __name__ == "__main__":
    unittest.main()
