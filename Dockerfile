FROM python:3.10-slim AS base

ENV POETRY_HOME="/opt/poetry"
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

ENV POETRY_VIRTUALENVS_IN_PROJECT="true"

RUN poetry install --no-interaction --without dev,test


FROM base AS runner

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && groupadd app \
 && useradd --shell /sbin/nologin --gid app app

ENV HOME="/home/app"

USER app

COPY --from=builder --chown=app:app $VENV $VENV

WORKDIR $HOME/app

COPY . .

CMD ["python", "-m", "speny.main"]
