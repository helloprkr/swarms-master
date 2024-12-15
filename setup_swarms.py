import os
import datetime
import shutil
from pathlib import Path

def create_ai_directories():
    """Create necessary AI documentation directories"""
    dirs = [
        ".ai/status",
        ".ai/session",
        ".ai/docs"
    ]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

def create_status_update():
    """Create a new status update file for today"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    status_file = f".ai/status/{today}.md"
    
    if not os.path.exists(status_file):
        with open(status_file, "w") as f:
            f.write(f"""# Status Update {today}

## Current State
- Project: Swarms Master
- Status: Setup and Documentation Phase

## Recent Decisions
- Implementing automated setup script
- Establishing documentation structure

## Next Steps
1. [ ] Review existing codebase
2. [ ] Document core components
3. [ ] Set up development environment
4. [ ] Implement automated testing

## Challenges/Blockers
- None identified yet

## Notes
- Initial setup in progress
""")

def main():
    # Create directory structure
    create_ai_directories()
    
    # Create initial status update
    create_status_update()
    
    print("✅ Project setup complete!")
    print("📝 Status update created in .ai/status/")

if __name__ == "__main__":
    main() 