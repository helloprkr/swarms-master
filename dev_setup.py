import subprocess
import sys
import os
import venv

def create_virtual_environment():
    """Create a virtual environment for the project"""
    venv_path = ".venv"
    print(f"🔧 Creating virtual environment in {venv_path}")
    
    try:
        venv.create(venv_path, with_pip=True)
        print("✅ Virtual environment created successfully")
    except Exception as e:
        print(f"❌ Error creating virtual environment: {e}")
        sys.exit(1)

def install_dependencies():
    """Install project dependencies"""
    print("📦 Installing dependencies...")
    
    pip_commands = [
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        [sys.executable, "-m", "pip", "install", "-e", "."],
    ]
    
    for cmd in pip_commands:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing dependencies: {e}")
            sys.exit(1)
    
    print("✅ Dependencies installed successfully")

def setup_pre_commit_hooks():
    """Set up pre-commit hooks for code quality"""
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        print("✅ Pre-commit hooks installed")
    except subprocess.CalledProcessError:
        print("❌ Failed to install pre-commit hooks")

def create_dev_config():
    """Create development configuration files"""
    configs = {
        ".flake8": """[flake8]
max-line-length = 120
exclude = .git,__pycache__,build,dist
""",
        "pyproject.toml": """[tool.black]
line-length = 120
target-version = ['py310']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
""",
        ".env.example": """# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# Anthropic Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key

# Workspace Configuration
WORKSPACE_DIR=agent_workspace
"""
    }
    
    for filename, content in configs.items():
        with open(filename, 'w') as f:
            f.write(content)
    
    print("✅ Development configuration files created")

def main():
    print("🚀 Swarms Development Environment Setup")
    
    create_virtual_environment()
    install_dependencies()
    setup_pre_commit_hooks()
    create_dev_config()
    
    print("\n🎉 Development environment setup complete!")
    print("Next steps:")
    print("1. Activate virtual environment: source .venv/bin/activate")
    print("2. Run tests: pytest")
    print("3. Start developing!")

if __name__ == "__main__":
    main() 