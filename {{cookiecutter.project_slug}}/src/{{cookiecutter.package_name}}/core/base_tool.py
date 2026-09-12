"""Base tool interface."""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class BaseProjectTool(ABC):
    """Interface that every project-specific tool must implement."""

    name: str
    description: str
    args_schema: type[BaseModel]

    @abstractmethod
    def execute(self,arguments: BaseModel) -> Any:
        """Perform the tool operation using validated arguments."""