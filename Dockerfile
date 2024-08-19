FROM python:slim

RUN pip install "django<5"

COPY src /src

WORKDIR /src

CMD python manage.py runserver 0.0.0.0:8888
