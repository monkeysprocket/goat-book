FROM python:slim

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR="/tmp/poetry_cache"

WORKDIR /src

COPY poetry.lock pyproject.toml /src/
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY src /src

RUN poetry install --without dev

CMD poetry run gunicorn --bind :8888 superlists.wsgi:application
