# n8n-flow-manager 🚀

**n8n-flow-manager** is a robust, production-ready Python SDK and CLI for the [n8n automation platform](https://n8n.io/). Unlike simple HTTP wrappers, this package is designed for **DevOps workflows**, providing type-safe models, async operations, workflow templating, and CI/CD integration capabilities.

[![PyPI version](https://badge.fury.io/py/n8n-flow-manager.svg)](https://pypi.org/project/n8n-flow-manager/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-79%20passed-success)](https://github.com/Mgobeaalcoba/n8n-flow-manager)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](https://github.com/Mgobeaalcoba/n8n-flow-manager)

---

## ✨ Features

### Core Capabilities

- **⚡ Async-First Design**: Built on `httpx` for high-performance async operations
- **🛡️ Type Safety**: Complete Pydantic models for workflows, executions, and credentials
- **🔄 Smart Polling**: Execute workflows and wait for completion with intelligent status checking
- **📝 Jinja2 Templating**: Inject environment-specific variables into workflow definitions
- **🤖 Powerful CLI**: Terminal commands for backup, deploy, sync, and manage workflows
- **🔐 Secure**: API key authentication with proper error handling and retries
- **📦 Zero Config**: Works with environment variables or explicit configuration

### What Makes It Different?

| Feature | n8n-flow-manager | Generic HTTP Clients |
|---------|------------------|---------------------|
| Type Validation | ✅ Pydantic models | ❌ Raw dicts |
| Async Support | ✅ Native asyncio | ⚠️ Sync only |
| Smart Execution | ✅ run_and_wait() | ❌ Manual polling |
| Templating | ✅ Jinja2 built-in | ❌ Not included |
| CLI Tools | ✅ Full featured | ❌ None |
| Error Handling | ✅ Custom exceptions | ⚠️ Generic errors |

---

## 📂 Project Structure

```
n8n-flow-manager/
├── src/
│   └── n8n_manager/
│       ├── __init__.py           # Public API exports
│       ├── client.py             # Main async client
│       ├── exceptions.py         # Custom error types
│       ├── api/                  # API modules by resource
│       │   ├── workflows.py      # Workflow operations
│       │   ├── executions.py     # Execution management
│       │   └── credentials.py    # Credential handling
│       ├── models/               # Pydantic data models
│       │   ├── workflow.py       # Workflow structures
│       │   ├── execution.py      # Execution states
│       │   └── credential.py     # Credential types
│       ├── cli/                  # Command-line interface
│       │   └── main.py           # Typer CLI app
│       └── utils/                # Helper utilities
│           └── templating.py     # Jinja2 template engine
├── tests/                        # Pytest test suite
├── examples/                     # Usage examples
├── pyproject.toml                # Poetry configuration
└── README.md                     # This file
```

---

## 🚀 Installation

### Requirements

- Python 3.9 or higher
- n8n instance (cloud or self-hosted)

### Global CLI Installation (Recommended)

Install globally using **pipx** (the best practice for Python CLI tools):

```bash
# Install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install n8n-flow-manager globally
pipx install n8n-flow-manager

# Verify installation
n8n-py --version
n8n-py --help
```

> **Note:** If you don't have pipx, you can also use `pip install --user n8n-flow-manager`, but pipx is recommended as it isolates the package in its own environment.

### Configuration

After installation, configure your n8n credentials using environment variables:

```bash
# Set your n8n credentials
export N8N_API_KEY="your_api_key_here"
export N8N_BASE_URL="https://your-instance.n8n.cloud"

# Test the connection
n8n-py health
```

**Optional:** To make credentials persistent, add them to your shell profile:

```bash
# For zsh (macOS default)
echo 'export N8N_API_KEY="your_api_key_here"' >> ~/.zshrc
echo 'export N8N_BASE_URL="https://your-instance.n8n.cloud"' >> ~/.zshrc
source ~/.zshrc

# For bash
echo 'export N8N_API_KEY="your_api_key_here"' >> ~/.bashrc
echo 'export N8N_BASE_URL="https://your-instance.n8n.cloud"' >> ~/.bashrc
source ~/.bashrc
```

### Getting Your API Key

1. Open your n8n instance
2. Go to **Settings** → **API**
3. Click **Create API Key**
4. Copy the key and use it in the configuration above

**That's it!** You're ready to use n8n-flow-manager 🎉

### For Developers

If you want to use n8n-flow-manager as a Python library in your projects:

```bash
# Install with pip
pip install n8n-flow-manager

# Use in your code
from n8n_manager import N8NClient
```

For contributing or development, see the [Development](#-development) section below.

---

## 🛠️ Usage Guide

### 1. Python SDK Usage

#### Basic Client Usage

```python
import asyncio
from n8n_manager import N8NClient

async def main():
    # Initialize client (reads from environment)
    async with N8NClient() as client:

        # List all active workflows
        workflows = await client.workflows.list(active=True)
        for wf in workflows:
            print(f"Workflow: {wf.name} (ID: {wf.id})")

        # Get specific workflow
        workflow = await client.workflows.get("workflow_id")
        print(f"Nodes: {len(workflow.nodes)}")

        # Execute workflow and wait for result
        execution = await client.executions.run_and_wait(
            workflow_id="workflow_id",
            timeout=60
        )
        print(f"Status: {execution.status}")
        print(f"Success: {execution.is_successful}")

asyncio.run(main())
```

#### Creating Workflows Programmatically

```python
from n8n_manager import N8NClient
from n8n_manager.models.workflow import Workflow, Node

async def create_simple_workflow():
    async with N8NClient() as client:
        workflow = Workflow(
            name="Python-Created Workflow",
            active=False,
            nodes=[
                Node(
                    name="Start",
                    type="n8n-nodes-base.start",
                    position=[250, 300],
                    parameters={}
                ),
                Node(
                    name="Set Data",
                    type="n8n-nodes-base.set",
                    position=[450, 300],
                    parameters={
                        "values": {
                            "string": [
                                {"name": "message", "value": "Hello from Python!"}
                            ]
                        }
                    }
                )
            ],
            connections={
                "Start": {
                    "main": [[{"node": "Set Data", "type": "main", "index": 0}]]
                }
            }
        )

        created = await client.workflows.create(workflow)
        print(f"Created workflow: {created.id}")
```

#### Using Templates

```python
from n8n_manager.utils.templating import load_workflow_from_file

# Load workflow with template variables
workflow = load_workflow_from_file(
    "templates/data_sync.json",
    variables={
        "environment": "production",
        "api_endpoint": "https://api.example.com",
        "timeout": 30
    }
)

async with N8NClient() as client:
    deployed = await client.workflows.create(workflow)
    print(f"Deployed: {deployed.name}")
```

### 2. CLI Usage

The CLI provides powerful commands for workflow management.

**Example Output:**

```bash
$ n8n-py health
✓ Connection healthy!
  API URL: https://n8n.example.com/

$ n8n-py list-workflows
                              Workflows (33 found)
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃ ID               ┃ Name                           ┃ Active ┃ Nodes ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━┩
│ 1RDHBsmLkkTptybX │ Production Data Sync           │ ✓      │ 6     │
│ 2V3iCBkiOAPVzrUr │ Customer Onboarding            │ ✗      │ 7     │
│ 8qGqx5TW1QA7T8P9 │ Error Notifications            │ ✓      │ 2     │
└──────────────────┴────────────────────────────────┴────────┴───────┘
```

#### Commands

```bash
# List all workflows
n8n-py list-workflows

# List only active workflows
n8n-py list-workflows --active
```

#### Get Workflow Details

```bash
# Display workflow info
n8n-py get-workflow <workflow_id>

# Save workflow to file
n8n-py get-workflow <workflow_id> --output workflow.json
```

#### Deploy Workflows

```bash
# Deploy from JSON file
n8n-py deploy workflow.json

# Deploy with template variables
n8n-py deploy template.json --var environment=prod --var timeout=30

# Deploy and activate immediately
n8n-py deploy workflow.json --activate
```

#### Backup Workflows

```bash
# Backup all workflows
n8n-py backup --output ./backups

# Backup only active workflows
n8n-py backup --output ./backups --active-only
```

#### Execute Workflows

```bash
# Execute and wait for completion
n8n-py execute <workflow_id>

# Execute without waiting
n8n-py execute <workflow_id> --no-wait

# Execute with input data
n8n-py execute <workflow_id> --input data.json
```

#### Activate/Deactivate

```bash
# Activate workflow
n8n-py activate <workflow_id>

# Deactivate workflow
n8n-py deactivate <workflow_id>
```

#### Health Check

```bash
# Verify connection to n8n
n8n-py health
```

---

## 📚 Advanced Examples

### CI/CD Integration

Use in GitHub Actions for automated deployments:

```yaml
# .github/workflows/deploy-n8n.yml
name: Deploy n8n Workflows

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install n8n-flow-manager
        run: pip install -e .

      - name: Deploy workflows
        env:
          N8N_API_KEY: ${{ secrets.N8N_API_KEY }}
          N8N_BASE_URL: ${{ secrets.N8N_BASE_URL }}
        run: |
          n8n-py deploy workflows/production.json --activate
```

### Environment-Specific Deployments

```python
import asyncio
from n8n_manager import N8NClient
from n8n_manager.utils.templating import load_workflow_from_file

ENVIRONMENTS = {
    "dev": {
        "api_endpoint": "https://dev.api.example.com",
        "webhook_path": "webhook-dev",
        "timeout": 10
    },
    "prod": {
        "api_endpoint": "https://api.example.com",
        "webhook_path": "webhook",
        "timeout": 30
    }
}

async def deploy_to_environment(env: str):
    workflow = load_workflow_from_file(
        "templates/api_workflow.json",
        variables=ENVIRONMENTS[env]
    )

    async with N8NClient() as client:
        deployed = await client.workflows.create(workflow)
        await client.workflows.activate(deployed.id)
        print(f"Deployed to {env}: {deployed.id}")

# Deploy to production
asyncio.run(deploy_to_environment("prod"))
```

### Monitoring and Logging

```python
async def monitor_executions(workflow_id: str):
    async with N8NClient() as client:
        executions = await client.executions.list(
            workflow_id=workflow_id,
            limit=50
        )

        for execution in executions:
            if execution.is_failed:
                print(f"❌ Failed: {execution.id} at {execution.started_at}")
            elif execution.is_successful:
                print(f"✅ Success: {execution.id}")
```

---

## 🧪 Testing

Run the test suite with pytest:

```bash
# Install dev dependencies
poetry install --with dev

# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src/n8n_manager --cov-report=html

# Run specific test file
poetry run pytest tests/test_client.py
```

---

## 🔧 Development

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/n8n-flow-manager.git
cd n8n-flow-manager

# Install with dev dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install

# Run linting
poetry run black src/ tests/
poetry run ruff src/ tests/

# Type checking
poetry run mypy src/
```

### Project Roadmap

- [x] Core client with async support
- [x] Pydantic models for type safety
- [x] Workflow, execution, and credential APIs
- [x] CLI with Typer
- [x] Jinja2 templating
- [x] Smart execution polling
- [ ] Webhook management API
- [ ] Tag management
- [ ] Bulk operations
- [ ] Workflow validation before deploy
- [ ] Integration tests with mock n8n server

---

## 📖 API Reference

### N8NClient

Main client for interacting with n8n API.

**Methods:**
- `workflows` - WorkflowAPI instance
- `executions` - ExecutionAPI instance
- `credentials` - CredentialAPI instance
- `health_check()` - Verify API connection

### WorkflowAPI

**Methods:**
- `list(active=None, tags=None)` - List workflows
- `get(workflow_id)` - Get workflow by ID
- `create(workflow)` - Create new workflow
- `update(workflow_id, workflow)` - Update workflow
- `delete(workflow_id)` - Delete workflow
- `activate(workflow_id)` - Activate workflow
- `deactivate(workflow_id)` - Deactivate workflow

### ExecutionAPI

**Methods:**
- `list(workflow_id=None, limit=100, status=None)` - List executions
- `get(execution_id)` - Get execution details
- `trigger_workflow(workflow_id, input_data=None)` - Trigger execution
- `wait_for_execution(execution_id, timeout=300)` - Wait for completion
- `run_and_wait(workflow_id, input_data=None, timeout=300)` - Trigger and wait
- `retry(execution_id)` - Retry failed execution
- `delete(execution_id)` - Delete execution

### CredentialAPI

**Methods:**
- `list(credential_type=None)` - List credentials
- `get(credential_id)` - Get credential by ID
- `create(credential)` - Create credential
- `update(credential_id, credential)` - Update credential
- `delete(credential_id)` - Delete credential

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Write tests for new features
- Follow existing code style (Black + Ruff)
- Update documentation as needed
- Add type hints to all functions
- Keep commits atomic and well-described

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [n8n](https://n8n.io/) - The workflow automation platform
- [httpx](https://www.python-httpx.org/) - Async HTTP client
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting

---

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/yourusername/n8n-flow-manager/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/n8n-flow-manager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/n8n-flow-manager/discussions)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io/)

---

## 🎯 Use Cases

### DevOps & CI/CD
- Automate workflow deployments across environments
- Version control your n8n workflows in Git
- Integrate with GitLab/GitHub Actions pipelines

### Disaster Recovery
- Scheduled backups of all workflows
- Quick restore capabilities
- Environment replication

### Multi-Tenant Management
- Programmatically create workflows for new clients
- Template-based workflow generation
- Bulk operations across workflows

### Monitoring & Observability
- Track execution success rates
- Monitor workflow health
- Automated alerting on failures

---

**Made with ❤️ for the n8n community**
