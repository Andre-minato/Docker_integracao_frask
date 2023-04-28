## Passos
#### 1 - Baixar imagem Mysql. 
* docker pull mysql:5.7
#### 2 - Criar conteiner para Mysql.
* docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=mudar123 -p 3307:3307 -d mysql:5.7
#### 3 - Acessar bash dentro do container especificar id do container
* docker exec -it e9ce83871c83 /bin/bash 
#### 4 - Iniciar o banco de dados Mysql / Após iniciar inserir a senha
* mysql -uroot -p
#### 5 - Criar um schema teste
* create schema teste;
#### 6 - Alterar schema criado
* use teste;
#### 7 - Criando tabela no Mysql
* CREATE TABLE tbl_user ( user_id BIGINT NOT NULL AUTO_INCREMENT, user_name VARCHAR(45) NULL, user_username VARCHAR(45) NULL, user_password VARCHAR(45) NULL, PRIMARY KEY (user_id));
#### 8 - Verificar se a tabela foi criada 
* show tables;

#### Comandos útils
##### 1 - Obter ip do banco de dados
* docker network inspect bridge + id conteiner
##### 2 - Obter os containeres que estão rodando.
* docker ps
##### 2 - Obter todos os containeres parado / Rodando.
* docker ps -a

#### Dependências
* pip install flask
* pip install flask-mysql
