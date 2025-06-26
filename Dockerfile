FROM python:3.13-slim
WORKDIR /app
RUN pip install --upgrade pip 
RUN apt-get update
RUN apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
COPY ./scripts/* /app/scripts/
COPY ./personal_assistant/* /app/
CMD ["gunicorn", "personal_assistant.wsgi:application", "--bind", "0.0.0.0:8002", "--workers", "3", "--timeout", "120"]