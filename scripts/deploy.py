"""Deployment script for Swarms."""
import subprocess
import os
from pathlib import Path

def check_requirements():
    """Check if all requirements are met."""
    required_files = [
        "vercel.json",
        "src/server.py",
        "requirements.txt"
    ]
    
    for file in required_files:
        if not Path(file).exists():
            raise FileNotFoundError(f"Missing required file: {file}")

def deploy():
    """Deploy to Vercel."""
    try:
        # Check requirements
        check_requirements()
        
        # Build and deploy
        subprocess.run(["vercel", "deploy", "--prod"], check=True)
        
        print("✅ Deployment successful!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    deploy() 