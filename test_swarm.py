import os
from swarms import Agent
from swarms.models import AnthropicChat
import time

def create_agent():
    try:
        # Initialize the model with error handling
        model = AnthropicChat(
            model_name="claude-2.1",
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.7,
            max_tokens=1000
        )

        # Create agent with proper configuration
        return Agent(
            agent_name="Test-Agent",
            system_prompt="You are a helpful test agent.",
            llm=model,
            max_loops=1,
            autosave=True,
            dashboard=False,
            verbose=True
        )
    except Exception as e:
        print(f"Error creating agent: {e}")
        return None

def test_agent(agent):
    if not agent:
        return "Failed to initialize agent"
    
    max_retries = 3
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            response = agent.run("Hello, can you help me test if you're working?")
            return f"Agent response: {response}"
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                return f"All attempts failed. Final error: {e}"

if __name__ == "__main__":
    # Verify environment variables
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        exit(1)
        
    # Create and test agent
    agent = create_agent()
    result = test_agent(agent)
    print(result)
