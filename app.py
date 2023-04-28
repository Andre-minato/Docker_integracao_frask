import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
   return render_template('cadastro.html')


@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
  nome = request.form['nome']
  email = request.form['email']
  senha = request.form['senha']
  if nome and email and senha:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
    conn.commit()
  return render_template('cadastro.html')



if __name__ == "__main__":
    app.run()
