FROM python:3.11-slim

# Usamos el directorio actual como directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry 2.1.1
RUN pip install poetry==1.8.2

# Agregar Poetry al PATH
ENV PATH="/root/.local/bin:$PATH"

# Configurar Poetry para no crear un entorno virtual
RUN poetry config virtualenvs.create false

# Copiar los archivos de configuración de Poetry
COPY pyproject.toml poetry.lock ./

# Instalar dependencias
RUN poetry lock && poetry install

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando para iniciar la aplicación Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0", "--server.port=8501"]