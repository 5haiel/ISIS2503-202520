FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

RUN sed -i 's/\r$//' /app/start.sh && chmod +x /app/start.sh

ENV PORT=8080
EXPOSE 8080

CMD ["sh","/app/start.sh"]
