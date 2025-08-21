# Base image: Python 3.10 slim para ligereza
FROM python:3.10-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto
COPY . .

# Expone el puerto donde corre Django
EXPOSE 8000

# Comando para correr: migraciones y servidor (gunicorn para prod, pero usamos runserver por simplicidad)
ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]