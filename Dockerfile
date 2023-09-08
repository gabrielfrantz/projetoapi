# versão da imagem do postgresql
FROM postgres:latest

# copia tudo que está na pasta db do computador e executa os scripts SQL na criação do banco de dados no container (create e insert)
COPY ./db/ /docker-entrypoint-initdb.d/



