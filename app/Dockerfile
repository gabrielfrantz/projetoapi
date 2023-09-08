# versão da imagem do postgresql
FROM python:latest

# cria um diretório novo dentro do container chamado app
WORKDIR /app

# realia a instalação dos seguintes pacotes
RUN pip install pyscopg2 psycopg2-binary flask

# copia tudo que está na pasta app do computador para dentro da pasta app criada no container
COPY . /app

# realiza a execução do servidor flask
CMD ["python","app/app.py"]
