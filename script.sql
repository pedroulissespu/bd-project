-- Criação do banco de dados
CREATE DATABASE Biblioteca;
USE Biblioteca;

-- Tabela Usuário
CREATE TABLE IF NOT EXISTS Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Tipo ENUM('Aluno', 'Professor') NOT NULL
);

-- Tabela Aluno (especialização de Usuário)
CREATE TABLE IF NOT EXISTS Aluno (
    ID_Usuario INT PRIMARY KEY,
    Curso VARCHAR(100) NOT NULL,
    Matricula VARCHAR(20) NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);

-- Tabela Professor (especialização de Usuário)
CREATE TABLE IF NOT EXISTS Professor (
    ID_Usuario INT PRIMARY KEY,
    Departamento VARCHAR(100) NOT NULL,
    Titulacao VARCHAR(100) NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);

-- Tabela Editora
CREATE TABLE IF NOT EXISTS Editora (
    ID_Editora INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100) NOT NULL
);

-- Tabela Livro
CREATE TABLE IF NOT EXISTS Livro (
    ID_Livro INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(200) NOT NULL,
    AnoPublicacao INT NOT NULL,
    ID_Editora INT NOT NULL,
    FOREIGN KEY (ID_Editora) REFERENCES Editora(ID_Editora)
);

-- Tabela Autor
CREATE TABLE IF NOT EXISTS Autor (
    ID_Autor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL
);

-- Tabela Livro_Autor (relacionamento N:N entre Livro e Autor)
CREATE TABLE IF NOT EXISTS Livro_Autor (
    ID_Livro INT,
    ID_Autor INT,
    PRIMARY KEY (ID_Livro, ID_Autor),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);

-- Tabela Categoria
CREATE TABLE IF NOT EXISTS Categoria (
    ID_Categoria INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL
);

-- Tabela Livro_Categoria (relacionamento N:N entre Livro e Categoria)
CREATE TABLE IF NOT EXISTS Livro_Categoria (
    ID_Livro INT,
    ID_Categoria INT,
    PRIMARY KEY (ID_Livro, ID_Categoria),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);

-- Tabela Disciplina
CREATE TABLE IF NOT EXISTS Disciplina (
    ID_Disciplina INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Curso VARCHAR(100) NOT NULL
);

-- Tabela Livro_Disciplina (relacionamento N:N entre Livro e Disciplina)
CREATE TABLE IF NOT EXISTS Livro_Disciplina (
    ID_Livro INT,
    ID_Disciplina INT,
    PRIMARY KEY (ID_Livro, ID_Disciplina),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID_Disciplina)
);

-- Tabela Fornecedor
CREATE TABLE IF NOT EXISTS Fornecedor (
    ID_Fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Telefone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

-- Tabela Exemplar
CREATE TABLE IF NOT EXISTS Exemplar (
    ID_Exemplar INT AUTO_INCREMENT PRIMARY KEY,
    Localizacao VARCHAR(100) NOT NULL,
    ID_Livro INT NOT NULL,
    ID_Fornecedor INT NOT NULL,
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Fornecedor) REFERENCES Fornecedor(ID_Fornecedor)
);

-- Tabela Reserva
CREATE TABLE IF NOT EXISTS Reserva (
    ID_Reserva INT AUTO_INCREMENT PRIMARY KEY,
    DataReserva DATE NOT NULL,
    ID_Usuario INT NOT NULL,
    ID_Exemplar INT NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar)
);

-- Tabela Emprestimo
CREATE TABLE IF NOT EXISTS Emprestimo (
    ID_Emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    DataEmprestimo DATE NOT NULL,
    DataDevolucao DATE NOT NULL,
    ID_Exemplar INT NOT NULL,
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar)
);
