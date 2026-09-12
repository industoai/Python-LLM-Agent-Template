"""Run the main code for {{cookiecutter.project_name}}."""

import logging
from pathlib import Path
from typing import Any

import click

from {{cookiecutter.package_name}} import __version__
from {{cookiecutter.package_name}}.application import Application
from {{cookiecutter.package_name}}.config import load_config
from {{cookiecutter.package_name}}.loggings import config_logger
from {{cookiecutter.package_name}}.models import create_model


logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version=__version__)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Shorthand for info/debug/warning/error loglevel (-v/-vv/-vvv/-vvvv)",
)
def {{cookiecutter.package_name}}_cli(verbose: int) -> None:
    """Anomaly Detection of corks using hyper spectral imaging"""
    if verbose == 1:
        log_level = 10
    elif verbose == 2:
        log_level = 20
    elif verbose == 3:
        log_level = 30
    else:
        log_level = 40
    config_logger(log_level)


@{{cookiecutter.package_name}}_cli.command()
@click.version_option(version=__version__)
@click.argument("user_input",required=False)
@click.option(
    "-c",
    "--config-path",
    type=click.Path(
        path_type=Path,
        exists=True,
        dir_okay=False,
        readable=True,
    ),
    default=Path("config.json"),
    show_default=True,
    help="Path to the JSON configuration file.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help=(
        "Increase logging detail. Use -v for INFO "
        "and -vv for DEBUG."
    ),
)
def run(user_input: str | None, config_path: Path) -> None:
    """{{cookiecutter.project_description}}."""

    if user_input is None:
        user_input = click.prompt("User",type=str)

    user_input = user_input.strip()

    if not user_input:
        raise click.UsageError("The user input cannot be empty.")

    try:
        logger.debug("Loading configuration from %s.",config_path)
        config = load_config(config_path)
        logger.debug("Creating provider=%s model=%s.",config.model.provider,config.model.name)
        model = create_model(config)
        application = Application(model=model,config=config)
        logger.info("Processing the user request.")
        result: Any = application.run(user_input)
        click.echo(result)
        logger.info("The request was completed successfully.")

    except Exception as exc:
        logger.exception("The application failed.")
        raise click.ClickException(str(exc)) from exc
