# projeto devops
# Criar uma API com o Flask para fazer:
    # localhost/emails (GET) - listar todos os e-mails cadastrados
    # localhost/emails/id (GET) - listar um email específico
    # localhost/emails/id (PUT) - editar um email específico
    # localhost/emails/id (POST) - cadastrar um novo email
    # localhost/emails/id (DELETE) - deletar um email específico
# URL base vai ser: localhost
# testar via POSTMAN

import psycopg2

from flask import Flask, jsonify, request # importa o Flask (servidor), importa o jsonify (formato de JSON) e o request (acessar os dados - requisições)

app = Flask(__name__) # criando uma aplicação com o nome de Flask

def conectadb(): #conexao com o banco de dados postgres
    conexao = psycopg2.connect(host="localhost",
                               database="cadastros",
                               user="postgres",
                               password="postgres",
                               port=5050)
    return conexao

# (GET)
@app.route('/emails',methods=['GET']) # aqui é definido qual URL que vai chamar esse médodo
def obter_emails(): # método para listar todos os e-mails cadastrados
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = f'SELECT * FROM tabela;'
        cursor.execute(sql)
        dados = cursor.fetchall()
        registros = []
        for i in dados:
            registros.append(i)
        return(jsonify(registros))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao listar os e-mails cadastrados!\n", error)
        cursor.close()
        return 1
    
# (GET)
@app.route('/emails/<int:id>',methods=['GET']) # aqui é definido qual URL que vai chamar esse médodo
def obter_email(id): # método para listar um email específico
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = f'SELECT * FROM tabela WHERE id = {id};'
        cursor.execute(sql)
        dados = cursor.fetchall()
        return(jsonify(dados))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao listar o e-mail cadastrado!\n", error)
        cursor.close()
        return 1

# (PUT)
@app.route('/emails/<int:id>',methods=['PUT']) # aqui é definido qual URL que vai chamar esse médodo
def editar_email(id): # método para atualizar um email específico
    novo_email = request.form.get('email') # recebe o valor do email a ser alterado pelo usuário (testado via postman em form-data)
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = 'UPDATE tabela SET email = \'{}\' WHERE id = \'{}\''.format(novo_email,id)
        cursor.execute(sql)
        conexao.commit()
        newsql = f'SELECT * FROM tabela;'
        cursor.execute(newsql)
        dados = cursor.fetchall()
        return(jsonify(dados))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao atualizar o e-mail!\n", error)
        cursor.close()
        return 1

# (POST)
@app.route('/emails',methods=['POST']) # aqui é definido qual URL que vai chamar esse médodo
def cadastrar_email(): # método para cadastrar um novo email
    novo_email = request.form.get('email') # recebe o valor do email a ser cadastrado pelo usuário (testado via postman em form-data)
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = 'INSERT INTO tabela VALUES (DEFAULT,\'{}\')'.format(novo_email)
        cursor.execute(sql)
        conexao.commit()
        newsql = f'SELECT * FROM tabela;'
        cursor.execute(newsql)
        dados = cursor.fetchall()
        return(jsonify(dados))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao cadastrar novo e-mail!\n", error)
        cursor.close()
        return 1

# (DELETE)
@app.route('/emails/<int:id>',methods=['DELETE']) # aqui é definido qual URL que vai chamar esse médodo
def deletar_email(id): # método para deletar um email específico
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = f'DELETE FROM tabela WHERE id = {id};'
        cursor.execute(sql)
        conexao.commit()
        newsql = f'SELECT * FROM tabela;'
        cursor.execute(newsql)
        dados = cursor.fetchall()
        return(jsonify(dados))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao deletar e-mail!\n", error)
        cursor.close()
        return 1

app.run(port=4000,host='localhost',debug=True) # define em qual porta ele vai rodar e em qual host (localhost)