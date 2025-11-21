# Imagen oficial de Python
FROM python:3.10-slim

# Evitar que Python genere archivos .pyc y hacer stdout sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear directorio de la app
WORKDIR /app

# Instalar dependencias del sistema si ANTLR o fastapi lo requiere
RUN apt-get update && apt-get install -y \
    default-jre \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY requirements.txt /app/

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . /app/

# Exponer puerto del servidor
EXPOSE 8000

# Comando de arranque (FastAPI con Uvicorn)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]