# Запустить контейнер можно командой
# sudo docker run -it -p 8000:8000 app

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000