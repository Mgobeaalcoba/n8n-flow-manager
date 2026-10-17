# AGENTS.md — n8n-flow-manager

Guide for any agent (Claude Code, Codex, Antigravity/Gemini, Copilot). The bridges `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md` point to this file.

## What it is

Production-ready Python SDK and CLI for the [n8n automation platform](https://n8n.io/): type-safe Pydantic models, async operations, workflow templating and CI/CD helpers. Published on PyPI as `n8n-flow-manager`. Public repo, MIT license.

## Layout

- `src/n8n_manager/` — package code. `tests/` — test suite. `examples/` — usage examples.
- `Makefile` — dev commands (Poetry under the hood). `pyproject.toml` — metadata and tool config.
- `CHANGELOG.md` — keep it updated with every user-visible change.

## Commands

```bash
make install-dev   # poetry install --with dev (+ pre-commit hooks)
make test          # pytest
make test-cov      # pytest with coverage report
make check         # lint (ruff) + format (black) + type check (mypy)
make build         # build the package
```

## Rules

- Prefer `make` targets over ad-hoc commands; keep the suite green (79+ tests, ~85% coverage bar).
- Type-safe models and full type hints; English for code, docs and commit messages.
- Never commit credentials or `.env`; examples and templates use placeholders.
- Version bumps touch `pyproject.toml` + `CHANGELOG.md` together; publishing (`make publish`) is an owner decision only.

## Status

Published and stable (PyPI); last activity: 08/09/2026.

## Session memory

- `memory/STATE.md` (current snapshot) and `memory/LOG.md` (append-only history).
- When closing a session with changes: update STATE, add the LOG entry and commit; `scripts/scan_secrets.py` stays manual for now (pre-existing findings to review).
