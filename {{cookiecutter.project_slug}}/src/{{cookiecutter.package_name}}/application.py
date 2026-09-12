"""Main application implementation."""

from typing import Any

from {{cookiecutter.package_name}}.core.base_application import BaseApplication

{% if cookiecutter.project_type == "basic_llm" %}
from {{cookiecutter.package_name}}.prompts import PromptLoader
{% endif %}

{% if cookiecutter.project_type != "basic_llm" %}
from {{cookiecutter.package_name}}.agents.project_agent import ProjectAgent
from {{cookiecutter.package_name}}.tools.registry import create_tools
{% endif %}

{% if cookiecutter.project_type == "multi_agent" %}
from {{cookiecutter.package_name}}.agents.team import ProjectTeam
{% endif %}


class Application(BaseApplication):
    """Main application implementation."""

    def run(self,user_input: str) -> Any:
        """Process one user request."""

{% if cookiecutter.project_type == "basic_llm" %}
        system_prompt = PromptLoader().load("system")

        response = self.model.invoke(
            [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ]
        )

        return response.content

{% elif cookiecutter.project_type == "single_agent" %}
        agent = ProjectAgent(model=self.model,tools=create_tools())
        return agent.invoke(user_input)

{% elif cookiecutter.project_type == "multi_agent" %}
        team = ProjectTeam(model=self.model,tools=create_tools())
        return team.invoke(user_input)

{% endif %}