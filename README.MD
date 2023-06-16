# README.md

# neoway-data-services

## Instruções

Siga as etapas abaixo para configurar e executar o projeto **neoway-data-services**.

### Pré-requisitos

Certifique-se de ter o Docker instalado em seu sistema antes de prosseguir. Você pode encontrar informações sobre como instalar o Docker em: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

### Passos

1. **Subir o banco de dados**

   Execute o seguinte comando para iniciar o banco de dados em um contêiner Docker:

   ```shell
   docker-compose up -d

2. **Construir a imagem do serviço**

    Para construir a imagem Docker para o serviço neoway-data-services, execute o seguinte comando:

    docker build -t neoway-data-services .

3. **Executar o serviço**

    Finalmente, para executar o serviço neoway-data-services, use o seguinte comando:
    docker run neoway-data-services

4 **Em seguida verificar os dados extraidos para o banco**
    Verifique os dados no banco !!
