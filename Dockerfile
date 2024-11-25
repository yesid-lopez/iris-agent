FROM python:3.12-slim

RUN pip install "poetry"

WORKDIR /app

COPY iris iris
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false

RUN poetry install

COPY .env .env

CMD streamlit run iris/streamlit/app.py
