FROM python:3.11

# Copia os arquivos de requisitos para o diretório de trabalho
COPY . /app

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Update package lists and install dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential libpq-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN python ./init_db.py

# Copy the rest of the application code
COPY . .


# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "server.py"]
