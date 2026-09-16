"""Resolve a writable home dir for standalone skill scripts.

Skill scripts may run outside the agent process (system Python, nix env,
CI) where agent-specific helpers are not importable. This module provides a
small ``get_skills_home()`` contract without requiring them on ``sys.path``.
"""
from __future__ import annotations

import os
from pathlib import Path


def get_skills_home() -> Path:
    """Return the skills data directory (default: ``~/.local/share/agent-skills``)."""
    val = os.environ.get("AGENT_SKILLS_HOME", "").strip()
    return Path(val) if val else Path.home() / ".local/share/agent-skills"
