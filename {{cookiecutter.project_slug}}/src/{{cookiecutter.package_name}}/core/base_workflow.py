"""Base workflow interface."""

from abc import ABC, abstractmethod
from typing import Any


class BaseProjectWorkflow(ABC):
    """Interface that every LangGraph workflow must implement."""

    def __init__(self) -> None:
        """Initialize the workflow and compile the graph."""
        self._graph = self.build()

    @abstractmethod
    def build(self) -> Any:
        """Construct and compile the workflow graph."""

    def invoke(self,initial_state: dict[str, Any]) -> dict[str, Any]:
        """Run the compiled workflow."""
        return self._graph.invoke(initial_state)