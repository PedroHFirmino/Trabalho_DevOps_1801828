CREATE DATABASE IF NOT EXISTS cadastro_alunos;

USE cadastro_alunos;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ra VARCHAR(20) NOT NULL UNIQUE
);