import unittest
import sys
from pathlib import Path


class TestEnvironmentSetup(unittest.TestCase):
    def setUp(self):
        self.root_dir = Path(__file__).parent.parent
        self.required_dirs = [
            ".ai/status",
            ".ai/session",
            ".ai/docs",
            "tests",
            "swarms",
        ]
        self.required_files = [
            "requirements.txt",
            "setup.py",
            "dev_setup.py",
            ".github/workflows/ci.yml",
            "DEVELOPMENT.md",
        ]

    def test_directory_structure(self):
        """Verify all required directories exist"""
        for dir_path in self.required_dirs:
            full_path = self.root_dir / dir_path
            self.assertTrue(
                full_path.exists(), f"Required directory {dir_path} does not exist"
            )

    def test_required_files(self):
        """Verify all required files exist"""
        for file_path in self.required_files:
            full_path = self.root_dir / file_path
            self.assertTrue(
                full_path.exists(), f"Required file {file_path} does not exist"
            )

    def test_python_version(self):
        """Verify Python version meets requirements"""
        version = sys.version_info
        self.assertTrue(
            version.major == 3 and version.minor >= 10,
            f"Python version 3.10+ required, got {version.major}.{version.minor}",
        )


if __name__ == "__main__":
    unittest.main()
