"""Project-specific tool placeholder."""

from typing import Any

from pydantic import BaseModel, Field

from ..core.base_tool import BaseProjectTool


class ProjectToolInput(BaseModel):
    """Replace these fields with the required tool inputs."""

    value: str = Field(description=("Replace this field with a project-specific input."))


class ProjectTool(BaseProjectTool):
    """Replace this placeholder with a project-specific tool."""

    name = "project_tool"
    description = "Replace this text with a precise description of when the agent should use the tool."
    args_schema = ProjectToolInput

    def execute(self, arguments: BaseModel) -> Any:
        """Perform the project-specific operation."""
        raise NotImplementedError("Implement the project-specific tool operation.")