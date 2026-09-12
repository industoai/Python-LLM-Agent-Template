"""Check the validity of the package_name and project_slug before generating the project."""

import re
import sys


PACKAGE_NAME = "{{ cookiecutter.package_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
VERSION = "{{cookiecutter.version}}"


if not re.fullmatch(r"[a-z][a-z0-9_]*", PACKAGE_NAME):
    print(
        "package_name must start with a lowercase letter and contain only "
        "lowercase letters, numbers, and underscores."
    )
    sys.exit(1)


if not re.fullmatch(r"[a-z][a-z0-9-]*", PROJECT_SLUG):
    print(
        "project_slug must start with a lowercase letter and contain only "
        "lowercase letters, numbers, and hyphens."
    )
    sys.exit(1)

if not re.fullmatch(r"\d+\.\d+\.\d+", VERSION):
    print(
        "version must use the semantic version format, for example 0.1.0."
    )
    sys.exit(1)
