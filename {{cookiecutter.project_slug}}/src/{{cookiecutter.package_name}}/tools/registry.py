"""Tool registration and LangChain adaptation."""

from typing import Any

from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel

from ..core.base_tool import BaseProjectTool
from ..tools.project_tool import ProjectTool


def to_langchain_tool(tool: BaseProjectTool) -> BaseTool:
    """Convert a project tool to a LangChain StructuredTool."""

    def invoke_tool(**kwargs: Any) -> Any:
        arguments: BaseModel = tool.args_schema.model_validate(kwargs)
        return tool.execute(arguments)

    return StructuredTool.from_function(
        func=invoke_tool,
        name=tool.name,
        description=tool.description,
        args_schema=tool.args_schema,
    )


def create_tools() -> list[BaseTool]:
    """Create the tools available to the project's agents."""

    project_tools: list[BaseProjectTool] = [ProjectTool()]
    return [to_langchain_tool(tool) for tool in project_tools]
