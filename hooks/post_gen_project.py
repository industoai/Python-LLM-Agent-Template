"""This checks the cookiecutter template variables and removes files that are not needed based on the user's selections."""

from pathlib import Path
import shutil


PROJECT_ROOT = Path.cwd()
PROJECT_TYPE = "{{ cookiecutter.project_type }}"
INCLUDE_DOCKER = "{{ cookiecutter.include_docker }}"


def remove(relative_path: str) -> None:
    """Remove a generated file or directory."""

    path = PROJECT_ROOT / relative_path

    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


if PROJECT_TYPE == "basic_llm":
    remove("src/{{cookiecutter.package_name}}/agents")
    remove("src/{{cookiecutter.package_name}}/tools")
    remove("src/{{cookiecutter.package_name}}/workflows")
    remove("src/{{cookiecutter.package_name}}/core/base_agent.py")
    remove("src/{{cookiecutter.package_name}}/core/base_tool.py")
    remove("src/{{cookiecutter.package_name}}/core/base_workflow.py")
    remove("src/{{cookiecutter.package_name}}/core/state.py")
    remove("prompts/agent.txt")
    remove("prompts/supervisor.txt")
    remove("tests/test_tool.py")
    remove("tests/test_workflow.py")

elif PROJECT_TYPE == "single_agent":
    remove("src/{{cookiecutter.package_name}}/agents/team.py")
    remove("prompts/system.txt")
    remove("prompts/supervisor.txt")

elif PROJECT_TYPE == "multi_agent":
    remove("prompts/system.txt")

if INCLUDE_DOCKER == "no":
    remove("Dockerfile")
