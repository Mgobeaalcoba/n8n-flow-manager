# Publishing to PyPI

Guide to publish n8n-flow-manager to PyPI.

---

## Prerequisites

1. **PyPI Account**: Create at https://pypi.org/account/register/
2. **API Token**: Generate at https://pypi.org/manage/account/token/
3. **Poetry Configured**: Set up PyPI credentials

---

## Setup PyPI Credentials

```bash
# Configure Poetry with PyPI token
poetry config pypi-token.pypi YOUR_PYPI_TOKEN

# Or use environment variable
export POETRY_PYPI_TOKEN_PYPI=YOUR_PYPI_TOKEN
```

---

## Pre-Publication Checklist

```bash
cd /Users/mgobea/Documents/Personal_Develop/n8n-flow-manager

# 1. Ensure all tests pass
poetry run pytest
# Should show: 79 passed, 85.39% coverage

# 2. Check package can be built
poetry build

# 3. Verify package contents
tar -tzf dist/n8n_flow_manager-0.1.0.tar.gz | head -20

# 4. Check metadata
poetry check

# 5. Verify README renders well
# Preview at: https://github.com/mgobea/n8n-flow-manager
```

---

## Build Package

```bash
# Clean previous builds
rm -rf dist/ build/

# Build distribution files
poetry build

# This creates:
# - dist/n8n_flow_manager-0.1.0.tar.gz (source)
# - dist/n8n_flow_manager-0.1.0-py3-none-any.whl (wheel)
```

---

## Test Installation Locally

```bash
# Test in a clean virtual environment
python3 -m venv test_env
source test_env/bin/activate

# Install from local build
pip install dist/n8n_flow_manager-0.1.0-py3-none-any.whl

# Test it works
n8n-py --help

# Cleanup
deactivate
rm -rf test_env
```

---

## Publish to Test PyPI (Recommended First)

```bash
# Configure Test PyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi YOUR_TEST_PYPI_TOKEN

# Publish to Test PyPI
poetry publish -r testpypi

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ n8n-flow-manager

# Verify
n8n-py --help
```

---

## Publish to PyPI (Production)

```bash
# Make sure everything is ready
poetry check
poetry run pytest

# Publish to PyPI
poetry publish

# Confirm publication at:
# https://pypi.org/project/n8n-flow-manager/
```

---

## After Publication

### Update README.md

Add installation badge:

```markdown
[![PyPI version](https://badge.fury.io/py/n8n-flow-manager.svg)](https://pypi.org/project/n8n-flow-manager/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
```

### Users Can Install

```bash
# With pip
pip install n8n-flow-manager

# With poetry
poetry add n8n-flow-manager

# With pipx (for CLI)
pipx install n8n-flow-manager

# Then use:
n8n-py health
n8n-py list-workflows
```

---

## Version Updates

### For patch updates (0.1.0 → 0.1.1):

```bash
# Update version
poetry version patch

# Update CHANGELOG.md

# Commit
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 0.1.1"
git tag v0.1.1
git push && git push --tags

# Build and publish
poetry build
poetry publish
```

### For minor updates (0.1.0 → 0.2.0):

```bash
poetry version minor
# Then same steps as above
```

### For major updates (0.1.0 → 1.0.0):

```bash
poetry version major
# Then same steps as above
```

---

## Troubleshooting

### "Package already exists"
- Version already published
- Increment version: `poetry version patch`

### "Invalid credentials"
- Check token: `poetry config pypi-token.pypi`
- Regenerate token at PyPI

### "Build failed"
- Run: `poetry check`
- Fix any errors in pyproject.toml

---

## Commands Summary

```bash
# Build
poetry build

# Publish to Test PyPI
poetry publish -r testpypi

# Publish to PyPI
poetry publish

# Version bump
poetry version patch|minor|major
```

---

## After First Publication

Update README.md installation section:

```markdown
## Installation

```bash
pip install n8n-flow-manager
```

## Quick Start

```bash
# Configure
export N8N_API_KEY="your_key"
export N8N_BASE_URL="https://n8n.example.com"

# Use CLI
n8n-py health
n8n-py list-workflows
```

---

**Ready to publish!** 🚀

See: https://python-poetry.org/docs/libraries/#publishing-to-pypi
