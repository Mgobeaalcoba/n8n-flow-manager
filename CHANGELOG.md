# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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


## [0.1.2] - $(date +%Y-%m-%d)

### Fixed
- Corrected repository URLs in package metadata
- Updated README with PyPI installation as primary option
