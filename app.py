import os
from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
mysql.init_app(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')  # Supondo que sua página inicial seja index.html

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        if nome and email and senha:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('home')) 

    return render_template('cadastro.html')


@app.route('/listar', methods=['GET'])
def listar():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, user_name, user_username FROM tbl_user') 
        data = cursor.fetchall()  # Obtém os dados
        
        return render_template('lista.html', datas=data)

    except Exception as e:
        return json.dumps({'error': str(e)}), 500  # Retorna erro com status 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
