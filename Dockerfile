# versão da imagem do postgresql
FROM postgres:latest

# copia tudo que está na pasta db e executa os scripts SQL na criação do banco de dados (create e insert)
COPY ./db/ /docker-entrypoint-initdb.d/



