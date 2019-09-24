FROM jfloff/alpine-python:latest

COPY . /app

WORKDIR /app

RUN pip install -r -requirements

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]





