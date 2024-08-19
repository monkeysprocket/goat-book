FROM python:slim

RUN pip install "django<5" gunicorn whitenoise

COPY src /src

WORKDIR /src

CMD gunicorn --bind :8888 superlists.wsgi:application
