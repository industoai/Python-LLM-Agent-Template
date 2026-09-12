"""Project-specific LangGraph workflow."""

from typing import Any

from langgraph.graph import END, START, StateGraph

from ..core.base_agent import BaseProjectAgent
from ..core.base_workflow import BaseProjectWorkflow
from ..core.state import WorkflowState


class ProjectWorkflow(BaseProjectWorkflow):
    """General LangGraph workflow to extend for the project."""

    def __init__(self,agents: dict[str, BaseProjectAgent]) -> None:
        self.agents = agents
        super().__init__()

    def run_agent(self,state: WorkflowState) -> dict[str, Any]:
        """Run the agent selected in the workflow state."""
        agent_name = state.get("next_agent","project_agent")

        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}")
        agent = self.agents[agent_name]
        result = agent.invoke_messages(state.get("messages", []))

        return {
            "messages": result["messages"],
            "current_agent": agent_name,
            "result": result,
        }

    def build(self) -> Any:
        """Build and compile the workflow."""

        builder = StateGraph(WorkflowState)
        builder.add_node("agent",self.run_agent)
        builder.add_edge(START,"agent")
        builder.add_edge("agent",END)

        return builder.compile()