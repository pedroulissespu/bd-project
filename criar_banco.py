import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Tabela Usuário
cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuario (
    ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Tipo TEXT CHECK(Tipo IN ('Aluno', 'Professor')) NOT NULL
);
''')

# Tabela Aluno (especialização de Usuário)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Aluno (
    ID_Usuario INTEGER PRIMARY KEY,
    Curso TEXT NOT NULL,
    Matricula TEXT NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);
''')

# Tabela Professor (especialização de Usuário)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Professor (
    ID_Usuario INTEGER PRIMARY KEY,
    Departamento TEXT NOT NULL,
    Titulacao TEXT NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);
''')

# Tabela Editora
cursor.execute('''
CREATE TABLE IF NOT EXISTS Editora (
    ID_Editora INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cidade TEXT NOT NULL
);
''')

# Tabela Livro
cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro (
    ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    AnoPublicacao INTEGER NOT NULL,
    ID_Editora INTEGER NOT NULL,
    FOREIGN KEY (ID_Editora) REFERENCES Editora(ID_Editora)
);
''')

# Tabela Autor
cursor.execute('''
CREATE TABLE IF NOT EXISTS Autor (
    ID_Autor INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL
);
''')

# Tabela Livro_Autor (relacionamento N:N entre Livro e Autor)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro_Autor (
    ID_Livro INTEGER,
    ID_Autor INTEGER,
    PRIMARY KEY (ID_Livro, ID_Autor),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);
''')

# Tabela Categoria
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    ID_Categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL
);
''')

# Tabela Livro_Categoria (relacionamento N:N entre Livro e Categoria)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro_Categoria (
    ID_Livro INTEGER,
    ID_Categoria INTEGER,
    PRIMARY KEY (ID_Livro, ID_Categoria),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);
''')

# Tabela Disciplina
cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplina (
    ID_Disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL
);
''')

# Tabela Livro_Disciplina (relacionamento N:N entre Livro e Disciplina)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro_Disciplina (
    ID_Livro INTEGER,
    ID_Disciplina INTEGER,
    PRIMARY KEY (ID_Livro, ID_Disciplina),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID_Disciplina)
);
''')

# Tabela Fornecedor
cursor.execute('''
CREATE TABLE IF NOT EXISTS Fornecedor (
    ID_Fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Email TEXT NOT NULL
);
''')

# Tabela Exemplar
cursor.execute('''
CREATE TABLE IF NOT EXISTS Exemplar (
    ID_Exemplar INTEGER PRIMARY KEY AUTOINCREMENT,
    Localizacao TEXT NOT NULL,
    ID_Livro INTEGER NOT NULL,
    ID_Fornecedor INTEGER NOT NULL,
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Fornecedor) REFERENCES Fornecedor(ID_Fornecedor)
);
''')

# Tabela Reserva
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reserva (
    ID_Reserva INTEGER PRIMARY KEY AUTOINCREMENT,
    DataReserva TEXT NOT NULL,
    ID_Usuario INTEGER NOT NULL,
    ID_Exemplar INTEGER NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar)
);
''')

# Tabela Emprestimo
cursor.execute('''
CREATE TABLE IF NOT EXISTS Emprestimo (
    ID_Emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
    DataEmprestimo TEXT NOT NULL,
    DataDevolucao TEXT NOT NULL,
    ID_Exemplar INTEGER NOT NULL,
    FOREIGN KEY (ID_Exemplar) REFERENCES Exemplar(ID_Exemplar)
);
''')

# Gatilho para atualizar a data de devolução do empréstimo
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS atualizar_data_devolucao
BEFORE INSERT ON Emprestimo
FOR EACH ROW
BEGIN
    UPDATE Emprestimo SET DataDevolucao = DATE(DataEmprestimo, '+14 days') WHERE ID_Emprestimo = NEW.ID_Emprestimo;
END;
''')

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()

print("Banco de dados e tabelas criados com sucesso!")
