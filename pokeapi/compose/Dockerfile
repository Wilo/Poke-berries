FROM python:3.10-alpine

WORKDIR /app

# python:
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# pip:
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

# Install OS dependencies
RUN apk update && apk add --no-cache bash gcc musl-dev postgresql-dev python3-dev libffi-dev libpq-dev
RUN apk add --no-cache ca-certificates && update-ca-certificates
RUN pip install -U pip

# Install Poetry
RUN pip install poetry

COPY ../pyproject.toml /app/
COPY ../poetry.lock /app/

# Install depencencies
RUN poetry install

# Copy project
COPY ../ /app/

RUN mv compose/start.sh .
RUN rm -fr compose
CMD [ "./start.sh" ]
