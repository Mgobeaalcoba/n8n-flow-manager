# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2026-09-08

### Added
- `push` command: updates an **existing** workflow from a JSON file, using
  `WorkflowAPI.update()`. Reads the target ID from the `id` field of the file
  (as saved by `get-workflow --output` and `backup`) or from `--id`. This
  enables a pull → edit → push cycle with version control.
- `delete` command: deletes a workflow, showing its details and asking for
  confirmation first. `--yes` skips the prompt for CI usage.
- `list-workflows` now shows an **Archived** column, so archived workflows can
  be identified from the CLI.

### Fixed
- `deploy` and `push`: a `typer.Exit` raised for a controlled error was caught
  by the generic `except Exception` handler and printed as an empty
  `Error:` line. Controlled exits are now re-raised untouched.
- `push` detects archived workflows before calling the API and explains that
  they must be unarchived first, instead of surfacing the raw n8n error.

### Changed
- `deploy` docstring now states explicitly that it always creates a new
  workflow, to distinguish it from `push`.
- README: documents `push`, `delete` and the pre-existing `config` command,
  and fixes four links that pointed to `github.com/yourusername/...`.

## [0.1.0] - 2025-12-29

### Added
- Initial release of n8n-flow-manager
- Async-first N8NClient with httpx
- Complete Pydantic models for workflows, executions, and credentials
- WorkflowAPI with full CRUD operations
- ExecutionAPI with smart polling and run_and_wait functionality
- CredentialAPI for credential management
- Jinja2-based workflow templating system
- CLI application with Typer (n8n-py command)
- CLI commands: list-workflows, get-workflow, deploy, backup, execute, activate, deactivate, health
- Comprehensive test suite with pytest
- Usage examples for common scenarios
- Full documentation in README.md

### Features
- Type-safe workflow creation and validation
- Environment variable configuration support
- Async context manager support for client
- Custom exception hierarchy for better error handling
- Smart execution polling with configurable timeout
- Template rendering with variable injection
- Workflow backup and restore capabilities
- Rich terminal output with progress indicators

### Developer Tools
- Poetry-based dependency management
- Black code formatting
- Ruff linting
- MyPy type checking
- Pre-commit hooks configuration
- Comprehensive .gitignore

## [Unreleased]

### Planned
- Webhook management API
- Tag management operations
- Bulk workflow operations
- Workflow validation before deployment
- Integration tests with mock n8n server
- Workflow comparison and diff tools
- Export/import with dependency resolution
- Workflow versioning support
## [0.1.1] - 2025-12-29

### Fixed
- Corrected repository URLs to https://github.com/Mgobeaalcoba/n8n-flow-manager


## [0.1.2] - 2025-12-29

### Fixed
- Corrected repository URLs in package metadata
- Updated README with PyPI installation as primary option

## [0.1.3] - 2026-01-30

### Added
- New `config` command for interactive credential configuration
  - Auto-detects shell (zsh/bash)
  - Saves credentials to shell config or .env file
  - Tests connection after configuration
  - Secure input for API key (hidden)
  - Prevents overwriting without confirmation

### Fixed
- Fixed `--version` flag implementation (Click 8.3.x compatibility issue)
- Added Click version constraint (>=8.0.0,<8.2.0) to prevent future issues
- Synchronized version numbers between pyproject.toml and __init__.py
- Simplified README installation section to single method (pipx)

### Changed
- Cleaned up repository markdown files (kept only README.md and CHANGELOG.md)
- Updated .gitignore to exclude unnecessary markdown files
- Improved CLI help text and command descriptions

### Documentation
- Simplified installation instructions to use pipx only
- Added comprehensive configuration examples
- Improved getting started guide
