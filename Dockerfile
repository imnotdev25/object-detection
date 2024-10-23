FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary dependencies and geckodriver
RUN apt-get update && apt-get install -y wget curl

# Install Poetry and configure it
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Set work directory
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY app ./app
COPY templates ./templates
COPY models ./models

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]