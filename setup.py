from setuptools import setup, find_packages

setup(
    name="swarms",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "openai>=1.0.0",
        "anthropic>=0.7.0",
        "transformers>=4.30.0",
        "torch>=1.13.0",
        "numpy>=1.21.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "black>=23.3.0",
            "mypy>=1.3.0",
            "flake8>=6.0.0",
            "coverage>=7.2.0",
            "pre-commit>=3.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "myst-parser>=1.0.0",
        ],
    },
) 