FROM python:3.8-slim
RUN apt-get update
RUN python -m pip install --upgrade pip

# Install poetry:
RUN pip install poetry

# Copy in the config files:
COPY pyproject.toml ./
# Install only dependencies:
RUN poetry install --no-root --no-dev

# Copy in everything else and install:
COPY . .
RUN poetry install --no-dev

ENTRYPOINT ["source $(poetry env info --path)/bin/activate && pytemplates"]
