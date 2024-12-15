# Swarms AI Framework

A framework for building and orchestrating AI agents using various LLM providers (OpenAI, Anthropic, etc.).

## Current Status

The framework is currently operational with the following components:
- Basic Agent implementation with Anthropic Claude 2.1 integration
- Error handling for API calls
- Environment variable management
- Basic test implementation

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd swarms-master
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

4. Set up environment variables:
```bash
# Add to ~/.zshrc or ~/.bashrc
export ANTHROPIC_API_KEY="your-api-key-here"
```

5. Verify installation:
```bash
python test_swarm.py
```

## Known Issues and Solutions

1. OpenAI API Quota Error
   - Issue: "Error code: 429 - You exceeded your current quota"
   - Solution: Switched to Anthropic Claude model

2. Model Name Error
   - Issue: "claude-2 is a legacy model alias"
   - Solution: Updated to use "claude-2.1"

3. API Response Handling
   - Issue: Inconsistent response handling
   - Solution: Added proper error handling and response validation

## Development Notes

### Current Implementation
- Using Anthropic's Claude 2.1 model
- Basic agent framework with retry mechanism
- Error handling for API calls
- Environment variable validation

### Next Steps
1. Implement additional LLM providers
2. Add more comprehensive testing
3. Implement logging system
4. Add documentation for custom agent creation

## File Structure
```
src/
  swarms/
    models/
      anthropic_chat.py  # Anthropic implementation
      openai_chat.py     # OpenAI implementation
      __init__.py
    agent.py            # Base agent implementation
test_swarm.py          # Test implementation
```

## Testing

Run the basic test:
```bash
python test_swarm.py
```

Expected output:
```
🤖 Test-Agent processing task: Hello, can you help me test if you're working?
Agent response: [Success message from Claude]
```

## Troubleshooting

1. API Key Issues
   - Verify environment variables are set
   - Check API key validity
   - Ensure proper permissions

2. Model Issues
   - Verify model name ("claude-2.1")
   - Check API documentation for updates

3. Installation Issues
   - Clean install: `pip uninstall swarms && pip install -e .`
   - Verify Python version (3.8+)
   - Check dependency conflicts 