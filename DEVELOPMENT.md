# Swarms Development Guide

## 🛠 Development Environment Setup

### Prerequisites
- Python 3.10+
- pip
- virtualenv (optional)

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/kyegomez/swarms.git
cd swarms
```

2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install Dependencies
```bash
pip install -r requirements.txt
pip install -e .  # Install in editable mode
```

## 🧪 Testing

### Running Tests
To run the test suite, ensure you are in the virtual environment and execute:
```bash
pytest tests/
```

### Coverage Report
To check test coverage, run:
```bash
coverage run -m pytest
coverage report
```

### Continuous Integration
The project uses GitHub Actions for continuous integration. Tests will automatically run on every push and pull request.

## 📝 Code Quality

### Linting
```bash
flake8 swarms/
black --check swarms/
mypy swarms/
```

## 🔧 Development Workflow

1. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

2. Make changes

3. Run tests and linters
```bash
pytest
flake8
black --check .
```

4. Commit changes
```bash
git add .
git commit -m "Description of changes"
```

5. Push branch
```bash
git push -u origin feature/your-feature-name
```

## 📚 Documentation

Build documentation:
```bash
sphinx-build docs docs/_build
```

## 🤝 Contributing

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests. 