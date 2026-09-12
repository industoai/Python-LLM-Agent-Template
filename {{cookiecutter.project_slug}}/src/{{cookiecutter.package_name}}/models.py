"""Language-model initialization."""

import os
from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel

{% if cookiecutter.llm_provider == "openai" %}
from langchain_openai import ChatOpenAI
{% elif cookiecutter.llm_provider == "anthropic" %}
from langchain_anthropic import ChatAnthropic
{% elif cookiecutter.llm_provider == "ollama" %}
from langchain_ollama import ChatOllama
{% endif %}

from {{cookiecutter.package_name}}.config import ApplicationConfig




def require_environment_variable(variable_name: str) -> str:
    """Return a required environment variable."""
    value = os.getenv(variable_name)
    if not value:
        raise ValueError(f"Required environment variable is missing: {variable_name}")
    return value

def validate_provider(configured_provider: str) -> None:
    """Validate that the configured provider matches the generated code."""
    default_provider = "{{cookiecutter.llm_provider}}"
    if configured_provider != default_provider:
        raise ValueError(
            "The provider in config.json does not match the provider "
            "selected during project generation. "
            f"Expected '{default_provider}', but received "
            f"'{configured_provider}'."
        )

def create_model(config: ApplicationConfig) -> BaseChatModel:
    """Create the configured language model."""
    load_dotenv()
    model_config = config.model
    validate_provider(model_config.provider)

{% if cookiecutter.llm_provider == "openai" %}
    api_key = require_environment_variable("OPENAI_API_KEY")
    return ChatOpenAI(model=model_config.name,temperature=model_config.temperature,api_key=api_key)

{% elif cookiecutter.llm_provider == "anthropic" %}
    api_key = require_environment_variable("ANTHROPIC_API_KEY")

    return ChatAnthropic(model=model_config.name,temperature=model_config.temperature,api_key=api_key)

{% elif cookiecutter.llm_provider == "ollama" %}
    return ChatOllama(model=model_config.name,temperature=model_config.temperature)
{% endif %}
