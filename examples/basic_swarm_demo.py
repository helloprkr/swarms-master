import os
from dotenv import load_dotenv
from swarms import Agent
from swarms.models import OpenAIChat

def run_demo():
    """
    Basic demonstration of Swarms functionality
    """
    print("🚀 Starting Swarms Demo")
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")

    # Initialize the language model
    llm = OpenAIChat(
        model_name="gpt-4",
        openai_api_key=api_key
    )

    # Create a simple agent
    research_agent = Agent(
        agent_name="ResearchAgent",
        system_prompt="You are a research assistant specialized in AI and machine learning.",
        llm=llm,
        max_loops=1,
        verbose=True
    )

    # Run a simple task
    query = "What are the key benefits of multi-agent systems?"
    print(f"\n🤔 Asking agent: {query}")
    
    try:
        response = research_agent.run(query)
        print("\n✨ Agent Response:")
        print(response)
    except Exception as e:
        print(f"❌ Error during agent execution: {e}")

if __name__ == "__main__":
    run_demo() 