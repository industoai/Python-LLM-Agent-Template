"""Prompt-loading utilities."""

from pathlib import Path


class PromptLoader:
    """Load plain-text prompts from the prompt directory."""

    def __init__(self,prompt_directory: Path | None = None) -> None:
        self.prompt_directory = (prompt_directory or Path(__file__).resolve().parents[2] / "prompts")

    def load(self, name: str) -> str:
        """Load a prompt by name."""

        prompt_path = self.prompt_directory / f"{name}.txt"
        if not prompt_path.is_file():
            raise FileNotFoundError(f"Prompt does not exist: {prompt_path}")

        return prompt_path.read_text(encoding="utf-8").strip()

