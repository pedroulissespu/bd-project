-- Criação do banco de dados
CREATE DATABASE Biblioteca;
USE Biblioteca;

-- Tabela Usuário
CREATE TABLE Usuario (
    ID_Usuario INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

-- Tabela Aluno
CREATE TABLE Aluno (
    ID_Usuario INT PRIMARY KEY,
    Curso VARCHAR(100) NOT NULL,
    Matricula VARCHAR(20) NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);

-- Tabela Professor
CREATE TABLE Professor (
    ID_Usuario INT PRIMARY KEY,
    Departamento VARCHAR(100) NOT NULL,
    Titulacao VARCHAR(100) NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);

-- Tabela Editora
CREATE TABLE Editora (
    ID_Editora INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100) NOT NULL
);

-- Tabela Livro
CREATE TABLE Livro (
    ID_Livro INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(100) NOT NULL,
    Ano_Publicacao INT NOT NULL,
    ID_Editora INT,
    FOREIGN KEY (ID_Editora) REFERENCES Editora(ID_Editora)
);

-- Tabela Autor
CREATE TABLE Autor (
    ID_Autor INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL
);

-- Tabela Categoria
CREATE TABLE Categoria (
    ID_Categoria INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL
);

-- Tabela Livro_Autor (Relacionamento N:N entre Livro e Autor)
CREATE TABLE Livro_Autor (
    ID_Livro INT,
    ID_Autor INT,
    PRIMARY KEY (ID_Livro, ID_Autor),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);

-- Tabela Livro_Categoria (Relacionamento N:N entre Livro e Categoria)
CREATE TABLE Livro_Categoria (
    ID_Livro INT,
    ID_Categoria INT,
    PRIMARY KEY (ID_Livro, ID_Categoria),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);

-- Tabela Fornecedor
CREATE TABLE Fornecedor (
    ID_Fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Telefone VARCHAR(20),
    Email VARCHAR(100)
);

-- Tabela Exemplar
CREATE TABLE Exemplar (
    ID_Exemplar INT PRIMARY KEY AUTO_INCREMENT,
    Localizacao VARCHAR(100) NOT NULL,
    ID_Livro INT,
    ID_Fornecedor INT,
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Fornecedor) REFERENCES Fornecedor(ID_Fornecedor)
);

-- Tabela Reserva
CREATE TABLE Reserva (
    ID_Reserva INT PRIMARY KEY AUTO_INCREMENT,
    ID_Usuario INT,
    ID_Exemplar INT,
    Data_Reserva DATE NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar)
);

-- Tabela Empréstimo
CREATE TABLE Emprestimo (
    ID_Emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    ID_Exemplar INT,
    ID_Usuario INT,
    Data_Emprestimo DATE NOT NULL,
    Data_Devolucao DATE,
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);

-- Adicionando valores padrão
ALTER TABLE Editora MODIFY Cidade VARCHAR(100) NOT NULL DEFAULT 'Desconhecido';

-- Criando relacionamento ternário entre Usuario, Livro e Reserva
CREATE TABLE Reserva_Livro (
    ID_Reserva INT,
    ID_Livro INT,
    Quantidade INT DEFAULT 1,
    PRIMARY KEY (ID_Reserva, ID_Livro),
    FOREIGN KEY (ID_Reserva) REFERENCES Reserva(ID_Reserva),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro)
);

-- Criando um Gatilho (Trigger) para impedir empréstimos duplicados do mesmo exemplar
DELIMITER $$
CREATE TRIGGER antes_inserir_emprestimo
BEFORE INSERT ON Emprestimo
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1 FROM Emprestimo
        WHERE ID_Exemplar = NEW.ID_Exemplar AND Data_Devolucao IS NULL
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Este exemplar já está emprestado e não pode ser emprestado novamente.';
    END IF;
END $$
DELIMITER ;

-- Consulta avançada com GROUP BY e HAVING (Livros mais emprestados)
SELECT Livro.Titulo, COUNT(Emprestimo.ID_Emprestimo) AS Total_Emprestimos
FROM Emprestimo
JOIN Exemplar ON Emprestimo.ID_Exemplar = Exemplar.ID_Exemplar
JOIN Livro ON Exemplar.ID_Livro = Livro.ID_Livro
GROUP BY Livro.Titulo
HAVING COUNT(Emprestimo.ID_Emprestimo) > 5
ORDER BY Total_Emprestimos DESC;

-- Consulta usando ALL para encontrar editores que publicaram todos os livros de uma categoria específica
SELECT Editora.Nome
FROM Editora
WHERE NOT EXISTS (
    SELECT * FROM Livro_Categoria LC
    WHERE LC.ID_Categoria = 1
    AND NOT EXISTS (
        SELECT * FROM Livro
        WHERE Livro.ID_Livro = LC.ID_Livro AND Livro.ID_Editora = Editora.ID_Editora
    )
);

-- Consulta usando ANY para encontrar livros publicados por pelo menos uma editora específica
SELECT Livro.Titulo
FROM Livro
WHERE Livro.ID_Editora = ANY (
    SELECT Editora.ID_Editora FROM Editora WHERE Editora.Nome LIKE 'Editora Exemplo%'
);

-- Consulta com ordenação dinâmica (ASC ou DESC)
SELECT * FROM Livro ORDER BY Ano_Publicacao DESC;
