"""Verification script for Swarms setup."""
import os
from pathlib import Path
from typing import List, Tuple

def verify_structure() -> List[Tuple[str, bool]]:
    """Verify the project structure."""
    required_paths = [
        "src/swarms",
        "src/swarms/__init__.py",
        "src/swarms/agent.py",
        "src/swarms/models.py",
        "tests",
        "examples",
    ]
    
    results = []
    for path in required_paths:
        exists = Path(path).exists()
        results.append((path, exists))
    
    return results

def verify_imports() -> List[Tuple[str, bool]]:
    """Verify the imports work."""
    import_tests = [
        "from swarms import Agent",
        "from swarms import OpenAIChat",
    ]
    
    results = []
    for test in import_tests:
        try:
            exec(test)
            results.append((test, True))
        except Exception as e:
            print(f"Error importing {test}: {e}")
            results.append((test, False))
    
    return results

def main():
    """Run verification."""
    print("🔍 Verifying project structure...")
    structure_results = verify_structure()
    
    print("\nStructure check results:")
    for path, exists in structure_results:
        status = "✅" if exists else "❌"
        print(f"{status} {path}")
    
    print("\n🔍 Verifying imports...")
    import_results = verify_imports()
    
    print("\nImport check results:")
    for test, success in import_results:
        status = "✅" if success else "❌"
        print(f"{status} {test}")

if __name__ == "__main__":
    main()
