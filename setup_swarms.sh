#!/bin/bash

echo "🚀 Setting up Swarms development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the package in editable mode with all dependencies
pip install -e ".[dev,docs]"

# Install additional dependencies
pip install python-dotenv fastapi uvicorn

# Create necessary directories
mkdir -p src/swarms/models
mkdir -p tests
mkdir -p examples
mkdir -p .ai/status .ai/session .ai/docs

# Install Vercel CLI if not installed
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
fi

echo "🧪 Running verification..."
python verify.py

echo "🧪 Running tests..."
pytest tests/

echo "✨ Setup complete! You can now:"
echo "1. Run the demo: python examples/demo.py"
echo "2. Start the API server: uvicorn src.server:app --reload"
echo "3. Deploy to Vercel: python scripts/deploy.py" 