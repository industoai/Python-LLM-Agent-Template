FROM python:{{cookiecutter.python_version}}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml README.md config.json ./
COPY src ./src
COPY prompts ./prompts

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

CMD ["{{cookiecutter.package_name}}"]