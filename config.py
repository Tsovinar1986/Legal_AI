"""Configuration loader for the Legal aspect  System."""

from pathlib import Path

import yaml


def load_config() -> dict:
    """Load configuration from settings.yaml."""
    config_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


CONFIG = load_config()
