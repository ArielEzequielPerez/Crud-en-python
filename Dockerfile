# Dockerfile
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Expone el puerto por el que corre Django
EXPOSE 8000

# Comando por defecto al iniciar el contenedor
CMD ["python3", "sistema/manage.py", "runserver", "0.0.0.0:8000"]
