# Swarms AI Framework

A framework for building and orchestrating AI agents using various LLM providers (OpenAI, Anthropic, etc.).

## Features
- Basic Agent implementation with Anthropic Claude 2.1 integration
- Computer Use capability with virtual desktop environment
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

## Computer Use Setup

To use Anthropic's Claude AI Computer Use feature:

1. Prerequisites:
   - Install Docker Desktop for Mac from docker.com
   - Ensure you have a paid Anthropic account with API access

2. Set up the Computer Use demo:
```bash
git clone https://github.com/anthropics/anthropic-quickstarts.git
cd anthropic-quickstarts/computer-use-demo
```

3. Build and run the demo:
```bash
docker build -t computer-use-demo .
docker run -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY -p 3000:3000 computer-use-demo
```

4. Access the demo:
   - Open http://localhost:8080 in your browser
   - Interact with Claude in the virtual desktop environment

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

4. Docker Issues
   - Issue: "Cannot connect to Docker daemon"
   - Solution: Ensure Docker Desktop is running before building containers

## Development Notes

### Current Implementation
- Using Anthropic's Claude 2.1 model
- Basic agent framework with retry mechanism
- Error handling for API calls
- Environment variable validation
- Computer Use virtual desktop integration

### Next Steps
1. Implement additional LLM providers
2. Add more comprehensive testing
3. Implement logging system
4. Add documentation for custom agent creation
5. Enhance Computer Use capabilities

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

## Computer Use Testing

Test the Computer Use feature:
1. Launch the virtual desktop environment
2. Open the terminal in the virtual desktop
3. Try basic commands like:
   ```bash
   ls
   pwd
   echo "Hello Claude!"
   ```
4. Ask Claude to perform tasks in the environment

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

4. Docker Issues
   - Ensure Docker Desktop is running
   - Check Docker daemon status
   - Verify port 8080 is available