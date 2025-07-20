-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS flask_db;

-- Usa o banco
USE flask_db;

-- Cria a tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insere um usuário de exemplo
INSERT INTO usuarios (nome, email, senha)
VALUES ('João da Silva', 'joao@email.com', 'senha123');

-- Usuário 1
INSERT INTO usuarios (nome, email, senha)
VALUES ('Maria Oliveira', 'maria@email.com', '123456');

-- Usuário 2
INSERT INTO usuarios (nome, email, senha)
VALUES ('Carlos Souza', 'carlos@email.com', 'senha_segura');

-- Usuário 3
INSERT INTO usuarios (nome, email, senha)
VALUES ('Ana Lima', 'ana@email.com', 'minha_senha');

-- Usuário 4
INSERT INTO usuarios (nome, email, senha)
VALUES ('Pedro Costa', 'pedro@email.com', 'teste123');

-- Usuário 5
INSERT INTO usuarios (nome, email, senha)
VALUES ('Fernanda Rocha', 'fernanda@email.com', 'abc123');
