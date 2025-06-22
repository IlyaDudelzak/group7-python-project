FROM python:3.13-alpine

WORKDIR /personal_assistant

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY personal_assistant/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]