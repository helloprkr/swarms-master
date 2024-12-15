#!/bin/bash

echo "🚀 Setting up Swarms development environment..."

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the package in editable mode with all dependencies
pip install -e ".[dev,docs]"

# Create necessary directories
mkdir -p .ai/status .ai/session .ai/docs tests examples scripts

# Verify installation
python3 -c "import swarms; print('✅ Swarms package installed successfully')"

echo "✨ Environment setup complete!" 