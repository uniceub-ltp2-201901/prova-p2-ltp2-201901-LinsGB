#Gabriel Lins
#RA:21803169

# Importando bibliotecas
from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import *
from funcoes import *

# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cadastros'

@app.route("/")
def login():
    return render_template("home.html")

@app.route('/mostrar', methods=['post'])
def inserir():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    cursor = mysql.connect().cursor()
    url = gera_numeros(url_emuso(cursor))
    cadastrar(cursor, nome, senha, url)
    cursor.close()
    return render_template('mostrar_url.html', url=url)



if __name__ == '__main__':
    app.run(debug=True)
