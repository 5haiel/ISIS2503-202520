# Dockerfile (Python 3.9)
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app:/app/provesi

ENV PORT=8080
EXPOSE 8080

CMD ["sh","-c","python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn provesi.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers ${WORKERS:-3} --threads ${THREADS:-2} --timeout ${TIMEOUT:-60}"]
