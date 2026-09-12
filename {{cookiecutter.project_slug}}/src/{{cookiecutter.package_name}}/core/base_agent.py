"""Base agent interface."""

from abc import ABC, abstractmethod
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.tools import BaseTool


class BaseProjectAgent(ABC):
    """Interface that every project-specific agent must implement."""

    def __init__(self,model: BaseChatModel,tools: list[BaseTool]) -> None:
        """Initialize the agent with a language model and tools."""
        self.model = model
        self.tools = tools
        self._agent = self.build()

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the unique agent name."""

    @abstractmethod
    def build(self) -> Any:
        """Build and return the LangChain or LangGraph agent."""

    def invoke(self,user_input: str) -> dict[str, Any]:
        """Invoke the agent with a new user message."""
        return self.invoke_messages(
            [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        )

    def invoke_messages(self,messages: list[Any]) -> dict[str, Any]:
        """Invoke the agent with an existing message history."""
        return self._agent.invoke(
            {
                "messages": messages,
            }
        )