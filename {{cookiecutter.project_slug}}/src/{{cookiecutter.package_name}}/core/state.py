"""Shared LangGraph workflow state."""

from typing import Annotated, Any, TypedDict

from langgraph.graph.message import add_messages


class WorkflowState(TypedDict, total=False):
    """General state shared between workflow nodes."""

    messages: Annotated[list[Any],add_messages]
    current_agent: str
    next_agent: str
    result: Any
    error: str | None
    metadata: dict[str, Any]