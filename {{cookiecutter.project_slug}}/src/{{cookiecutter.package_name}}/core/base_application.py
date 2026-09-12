"""Base application interface."""

from abc import ABC, abstractmethod
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel

from ..config import ApplicationConfig


class BaseApplication(ABC):
    """Interface that the main application must implement."""

    def __init__(self, model: BaseChatModel, config: ApplicationConfig) -> None:
        """Initialize the application with a language model and configuration."""
        self.model = model
        self.config = config

    @abstractmethod
    def run(self, user_input: str) -> Any:
        """Process one user request and return the result."""