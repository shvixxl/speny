FROM python:3.11-slim AS base

ENV VIRTUAL_ENV="/opt/venv"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"


FROM base AS builder

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT="true"

ENV PATH="$POETRY_HOME/bin:$PATH"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
        curl \
 && curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /opt

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --without dev,test


FROM base AS runner

ENV HOME="/home/app"

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && groupadd app \
 && useradd --shell /sbin/nologin --gid app app

USER app

COPY --from=builder --chown=app:app $VIRTUAL_ENV $VIRTUAL_ENV

WORKDIR $HOME/app

COPY --chown=app:app . .

CMD ["python", "-m", "speny.main"]
