"""Multi-agent team configuration."""

from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.tools import BaseTool

from .agents.project_agent import ProjectAgent
from ..workflows.workflow import ProjectWorkflow


class ProjectTeam:
    """Create and coordinate the agents in a workflow."""

    def __init__(self,model: BaseChatModel,tools: list[BaseTool]) -> None:
        self.agents = {"project_agent": ProjectAgent(model=model,tools=tools)}
        self.workflow = ProjectWorkflow(agents=self.agents)

    def invoke(self,user_input: str) -> dict[str, Any]:
        """Run the multi-agent workflow."""

        initial_state = {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            "current_agent": "",
            "next_agent": "project_agent",
            "metadata": {},
        }

        return self.workflow.invoke(initial_state)