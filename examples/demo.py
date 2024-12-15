"""Basic demo of Swarms functionality."""
import os
from dotenv import load_dotenv
from swarms import Agent
from swarms.models import OpenAIChat

def main():
    """Run the demo."""
    # Load environment variables
    load_dotenv()
    
    # Initialize the model
    model = OpenAIChat(
        model_name="gpt-4",
        temperature=0.7
    )
    
    # Create an agent
    agent = Agent(
        agent_name="DemoAgent",
        system_prompt="You are a helpful AI assistant specialized in explaining complex topics simply.",
        llm=model,
        verbose=True
    )
    
    # Run a task
    task = "Explain what a swarm of AI agents is in simple terms."
    print("\n🤖 Running task:", task)
    
    response = agent.run(task)
    print("\n✨ Response:")
    print(response)

if __name__ == "__main__":
    main() 