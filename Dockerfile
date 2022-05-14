FROM python:3.8-slim AS build
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_HOME="/opt/poetry"
RUN curl -sSL https://install.python-poetry.org/ | python

# Add Poetry to the path
ENV PATH="$POETRY_HOME/bin:$PATH"

# Tell poetry to create a virtualenv in /.venv
RUN poetry config virtualenvs.in-project true

# Copy in the config files:
COPY pyproject.toml ./

# Install only dependencies:
RUN poetry install --no-root --no-dev

# Copy in source code else and install pytemplates:
COPY src/ src/
COPY README.md .
RUN poetry install --no-dev


FROM python:3.8-slim AS runtime
COPY --from=build .venv .venv
COPY --from=build src/ src/
ENV PATH=".venv/bin:$PATH"
ENTRYPOINT ["pytemplates"]
