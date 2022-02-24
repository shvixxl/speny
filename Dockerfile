FROM python:3.10-slim AS base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV POETRY_HOME="/etc/poetry"
ENV POETRY_VERSION="1.1.13"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

ENV VENV="/opt/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV/bin:$PATH"


FROM base AS builder

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
        curl \
 && curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /opt

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev


FROM base AS runner

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY --from=builder $VENV $VENV

WORKDIR /app

COPY . .

EXPOSE $PORT

CMD ["python", "-m", "speny.main"]
