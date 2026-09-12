"""Project-specific agent implementation."""

from typing import Any

from langchain.agents import create_agent

from ..core.base_agent import BaseProjectAgent
from ..prompts import PromptLoader


class ProjectAgent(BaseProjectAgent):
    """General tool-using agent to customize for the project."""

    @property
    def name(self) -> str:
        """Return the unique agent name."""
        return "project_agent"

    def build(self) -> Any:
        """Create the LangChain agent."""
        return create_agent(
            model=self.model,
            tools=self.tools,
            system_prompt=PromptLoader().load("agent"),
        )