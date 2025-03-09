-- Removendo qualquer conexão ativa com o banco antes de excluí-lo
DROP DATABASE IF EXISTS teste;

-- Criando o banco de dados
CREATE DATABASE IF NOT EXISTS teste;

-- Selecionando o banco de dados
USE teste;

-- Criando a tabela de usuários
CREATE TABLE IF NOT EXISTS tbl_user (
    id BIGINT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(45) NULL,
    user_username VARCHAR(45) NULL,
    user_password VARCHAR(45) NULL,
    PRIMARY KEY (id)
);
