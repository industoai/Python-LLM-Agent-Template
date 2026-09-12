"""Application configuration."""

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any
from dataclass_wizard import fromdict


@dataclass(frozen=True, slots=True)
class ModelConfig:
    """Language-model configuration."""

    provider: str
    name: str
    temperature: float = 0.0

    def __post_init__(self) -> None:
        """Validate the model configuration."""

        if self.provider not in {"openai","anthropic","ollama"}:
            supported = ", ".join(sorted({"openai","anthropic","ollama"}))
            raise ValueError(f"Unsupported model provider: {self.provider}. Supported providers: {supported}.")

        if not self.name.strip():
            raise ValueError("The model name cannot be empty.")

        if not 0.0 <= self.temperature <= 2.0:
            raise ValueError("The model temperature must be between 0.0 and 2.0.")


@dataclass(frozen=True, slots=True)
class ApplicationConfig:
    """Complete application configuration."""

    model: ModelConfig


def read_config_file(config_path: Path) -> dict[str, Any]:
    """Read configuration data from a JSON file."""

    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file does not exist: {config_path}")

    with config_path.open(mode="r",encoding="utf-8") as config_file:
        config_data = json.load(config_file)

    if not isinstance(config_data, dict):
        raise ValueError("The configuration root must be a JSON object.")

    return config_data


@lru_cache
def load_config(config_path: str | Path = "config.json") -> ApplicationConfig:
    """Load and parse the application configuration."""

    path = Path(config_path)
    config_data = read_config_file(path)
    return fromdict(ApplicationConfig,config_data)