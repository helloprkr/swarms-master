#!/usr/bin/env python3
import subprocess
import sys
import os
from pathlib import Path

class SetupValidator:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.venv_path = self.root_dir / ".venv"
        self.results = []

    def check_python_version(self):
        """Validate Python version >= 3.10"""
        version = sys.version_info
        return version.major == 3 and version.minor >= 10

    def check_virtual_environment(self):
        """Verify virtual environment exists and is activated"""
        in_venv = hasattr(sys, 'real_prefix') or (
            hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
        )
        venv_exists = self.venv_path.exists()
        return in_venv and venv_exists

    def check_dependencies(self):
        """Verify all required dependencies are installed"""
        try:
            import swarms
            import pytest
            import black
            import mypy
            return True
        except ImportError:
            return False

    def check_project_structure(self):
        """Verify project structure is correct"""
        required_dirs = [
            "src/swarms",
            "tests",
            "examples",
            "scripts",
            ".ai/status",
            ".ai/session",
            ".ai/docs"
        ]
        return all((self.root_dir / dir_path).exists() for dir_path in required_dirs)

    def validate(self):
        """Run all validation checks"""
        checks = {
            "Python Version": self.check_python_version,
            "Virtual Environment": self.check_virtual_environment,
            "Dependencies": self.check_dependencies,
            "Project Structure": self.check_project_structure
        }

        print("🔍 Validating Swarms Development Environment")
        print("-" * 50)

        all_passed = True
        for name, check_func in checks.items():
            try:
                passed = check_func()
                status = "✅" if passed else "❌"
                print(f"{status} {name}")
                all_passed = all_passed and passed
            except Exception as e:
                print(f"❌ {name} (Error: {e})")
                all_passed = False

        print("-" * 50)
        if all_passed:
            print("✨ All checks passed! Environment is properly configured.")
            print("\nNext steps:")
            print("1. Run the demo: python examples/basic_swarm_demo.py")
            print("2. Run tests: pytest tests/")
            print("3. Start development!")
        else:
            print("❌ Some checks failed. Please run setup_environment.sh to fix issues.")
            sys.exit(1)

if __name__ == "__main__":
    validator = SetupValidator()
    validator.validate() 