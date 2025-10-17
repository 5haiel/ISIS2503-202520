# Imagen base ligera
FROM python:3.12-slim

# Variables de entorno para Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear el directorio de la app
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . /app/

# Exponer el puerto 8000 (o el que uses)
EXPOSE 8080

# Comando de ejecución
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
