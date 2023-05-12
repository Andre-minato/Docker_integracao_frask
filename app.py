import os
from flask import Flask, render_template, request, json
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

@app.route('/list', methods=['POST','GET'])
def listar():
    try:
            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select user_name, user_username, user_password, user_password from tbl_user') 
            data = cursor.fetchall()
            print(data[0]);
            for x in range(len(data)):
                print(data[x])

            conn.commit()
            return render_template('lista.html', datas=data)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()


   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
