import unittest
import subprocess
from dev_setup import install_dependencies


class TestSetupSwarms(unittest.TestCase):
    def test_install_dependencies(self):
        """Test that dependencies can be installed without errors."""
        try:
            install_dependencies()
            self.assertTrue(True)  # If no exception is raised, the test passes
        except subprocess.CalledProcessError:
            self.fail("Dependency installation failed")


if __name__ == "__main__":
    unittest.main()
