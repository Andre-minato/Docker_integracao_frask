import mysql.connector
from mysql.connector import errorcode

print('Conectando......')
try:
    conn = mysql.connector.connect(
        host='172.17.0.2',
        user='root',
        password='mudar123'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado nome do usuério / Senha')
    else:
        print(err)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `teste`;")
cursor.execute("CREATE DATABASE `teste`;")
cursor.execute("USE `teste`;")

# Criando tabelas
TABLES = {}
TABLES['tbl_user'] = ('''
      CREATE TABLE `tbl_user`(
      `id` BIGINT NOT NULL AUTO_INCREMENT,
      `user_name` VARCHAR(45) NULL,
      `user_username` VARCHAR(45) NULL,
      `user_password` VARCHAR(45) NULL,
      PRIMARY KEY (id)
      )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


conn.commit()

cursor.close()
conn.close()


#CREATE TABLE tbl_user ( user_id BIGINT NOT NULL AUTO_INCREMENT, 
# user_name VARCHAR(45) NULL, user_username VARCHAR(45) NULL, 
# user_password VARCHAR(45) NULL, 
# PRIMARY KEY (user_id));
