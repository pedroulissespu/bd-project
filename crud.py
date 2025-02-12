import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",  # Endereço do servidor MySQL
        user="root",       # Usuário do MySQL
        password="root",  # Senha do MySQL
        database="Biblioteca"  # Nome do banco de dados
    )

# Operações CRUD para a tabela Usuario
def adicionar_usuario(nome, email, tipo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Usuario (Nome, Email, Tipo) VALUES (%s, %s, %s)"
    valores = (nome, email, tipo)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_usuario(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Usuario WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_usuario(id_usuario, nome, email, tipo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Usuario SET Nome = %s, Email = %s, Tipo = %s WHERE ID_Usuario = %s"
    valores = (nome, email, tipo, id_usuario)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_usuario(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Usuario WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return usuario

# Operações CRUD para a tabela Livro
def adicionar_livro(titulo, ano_publicacao, id_editora):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Livro (Titulo, AnoPublicacao, ID_Editora) VALUES (%s, %s, %s)"
    valores = (titulo, ano_publicacao, id_editora)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_livro(id_livro):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Livro WHERE ID_Livro = %s"
    valores = (id_livro,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_livro(id_livro, titulo, ano_publicacao, id_editora):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Livro SET Titulo = %s, AnoPublicacao = %s, ID_Editora = %s WHERE ID_Livro = %s"
    valores = (titulo, ano_publicacao, id_editora, id_livro)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_livro(id_livro):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Livro WHERE ID_Livro = %s"
    valores = (id_livro,)
    cursor.execute(sql, valores)
    livro = cursor.fetchone()
    cursor.close()
    conexao.close()
    return livro

# Operações CRUD para a tabela Editora
def adicionar_editora(nome, cidade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Editora (Nome, Cidade) VALUES (%s, %s)"
    valores = (nome, cidade)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_editora(id_editora):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Editora WHERE ID_Editora = %s"
    valores = (id_editora,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_editora(id_editora, nome, cidade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Editora SET Nome = %s, Cidade = %s WHERE ID_Editora = %s"
    valores = (nome, cidade, id_editora)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_editora(id_editora):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Editora WHERE ID_Editora = %s"
    valores = (id_editora,)
    cursor.execute(sql, valores)
    editora = cursor.fetchone()
    cursor.close()
    conexao.close()
    return editora

# Operações CRUD para a tabela Autor
def adicionar_autor(nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Autor (Nome) VALUES (%s)"
    valores = (nome,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_autor(id_autor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Autor WHERE ID_Autor = %s"
    valores = (id_autor,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_autor(id_autor, nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Autor SET Nome = %s WHERE ID_Autor = %s"
    valores = (nome, id_autor)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_autor(id_autor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Autor WHERE ID_Autor = %s"
    valores = (id_autor,)
    cursor.execute(sql, valores)
    autor = cursor.fetchone()
    cursor.close()
    conexao.close()
    return autor

# Operações CRUD para a tabela Exemplar
def adicionar_exemplar(localizacao, id_livro, id_fornecedor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Exemplar (Localizacao, ID_Livro, ID_Fornecedor) VALUES (%s, %s, %s)"
    valores = (localizacao, id_livro, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_exemplar(id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Exemplar WHERE ID_Exemplar = %s"
    valores = (id_exemplar,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_exemplar(id_exemplar, localizacao, id_livro, id_fornecedor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Exemplar SET Localizacao = %s, ID_Livro = %s, ID_Fornecedor = %s WHERE ID_Exemplar = %s"
    valores = (localizacao, id_livro, id_fornecedor, id_exemplar)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_exemplar(id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Exemplar WHERE ID_Exemplar = %s"
    valores = (id_exemplar,)
    cursor.execute(sql, valores)
    exemplar = cursor.fetchone()
    cursor.close()
    conexao.close()
    return exemplar

# Operações CRUD para a tabela Reserva
def adicionar_reserva(data_reserva, id_usuario, id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Reserva (DataReserva, ID_Usuario, ID_Exemplar) VALUES (%s, %s, %s)"
    valores = (data_reserva, id_usuario, id_exemplar)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_reserva(id_reserva):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Reserva WHERE ID_Reserva = %s"
    valores = (id_reserva,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_reserva(id_reserva, data_reserva, id_usuario, id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Reserva SET DataReserva = %s, ID_Usuario = %s, ID_Exemplar = %s WHERE ID_Reserva = %s"
    valores = (data_reserva, id_usuario, id_exemplar, id_reserva)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_reserva(id_reserva):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Reserva WHERE ID_Reserva = %s"
    valores = (id_reserva,)
    cursor.execute(sql, valores)
    reserva = cursor.fetchone()
    cursor.close()
    conexao.close()
    return reserva

# Operações CRUD para a tabela Aluno
def adicionar_aluno(id_usuario, curso, matricula):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Aluno (ID_Usuario, Curso, Matricula) VALUES (%s, %s, %s)"
    valores = (id_usuario, curso, matricula)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_aluno(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Aluno WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_aluno(id_usuario, curso, matricula):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Aluno SET Curso = %s, Matricula = %s WHERE ID_Usuario = %s"
    valores = (curso, matricula, id_usuario)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_aluno(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Aluno WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    aluno = cursor.fetchone()
    cursor.close()
    conexao.close()
    return aluno

# Operações CRUD para a tabela Professor
def adicionar_professor(id_usuario, departamento, titulacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Professor (ID_Usuario, Departamento, Titulacao) VALUES (%s, %s, %s)"
    valores = (id_usuario, departamento, titulacao)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_professor(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Professor WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_professor(id_usuario, departamento, titulacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Professor SET Departamento = %s, Titulacao = %s WHERE ID_Usuario = %s"
    valores = (departamento, titulacao, id_usuario)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_professor(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Professor WHERE ID_Usuario = %s"
    valores = (id_usuario,)
    cursor.execute(sql, valores)
    professor = cursor.fetchone()
    cursor.close()
    conexao.close()
    return professor

# Operações CRUD para a tabela Categoria
def adicionar_categoria(nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Categoria (Nome) VALUES (%s)"
    valores = (nome,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_categoria(id_categoria):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Categoria WHERE ID_Categoria = %s"
    valores = (id_categoria,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_categoria(id_categoria, nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Categoria SET Nome = %s WHERE ID_Categoria = %s"
    valores = (nome, id_categoria)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_categoria(id_categoria):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Categoria WHERE ID_Categoria = %s"
    valores = (id_categoria,)
    cursor.execute(sql, valores)
    categoria = cursor.fetchone()
    cursor.close()
    conexao.close()
    return categoria

# Operações CRUD para a tabela Livro_Autor
def adicionar_livro_autor(id_livro, id_autor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Livro_Autor (ID_Livro, ID_Autor) VALUES (%s, %s)"
    valores = (id_livro, id_autor)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_livro_autor(id_livro, id_autor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Livro_Autor WHERE ID_Livro = %s AND ID_Autor = %s"
    valores = (id_livro, id_autor)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_livro_autor(id_livro, id_autor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Livro_Autor WHERE ID_Livro = %s AND ID_Autor = %s"
    valores = (id_livro, id_autor)
    cursor.execute(sql, valores)
    livro_autor = cursor.fetchone()
    cursor.close()
    conexao.close()
    return livro_autor

# Operações CRUD para a tabela Livro_Categoria
def adicionar_livro_categoria(id_livro, id_categoria):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (%s, %s)"
    valores = (id_livro, id_categoria)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_livro_categoria(id_livro, id_categoria):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Livro_Categoria WHERE ID_Livro = %s AND ID_Categoria = %s"
    valores = (id_livro, id_categoria)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_livro_categoria(id_livro, id_categoria):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Livro_Categoria WHERE ID_Livro = %s AND ID_Categoria = %s"
    valores = (id_livro, id_categoria)
    cursor.execute(sql, valores)
    livro_categoria = cursor.fetchone()
    cursor.close()
    conexao.close()
    return livro_categoria

# Operações CRUD para a tabela Disciplina
def adicionar_disciplina(nome, curso):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Disciplina (Nome, Curso) VALUES (%s, %s)"
    valores = (nome, curso)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_disciplina(id_disciplina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Disciplina WHERE ID_Disciplina = %s"
    valores = (id_disciplina,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_disciplina(id_disciplina, nome, curso):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Disciplina SET Nome = %s, Curso = %s WHERE ID_Disciplina = %s"
    valores = (nome, curso, id_disciplina)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_disciplina(id_disciplina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Disciplina WHERE ID_Disciplina = %s"
    valores = (id_disciplina,)
    cursor.execute(sql, valores)
    disciplina = cursor.fetchone()
    cursor.close()
    conexao.close()
    return disciplina

# Operações CRUD para a tabela Livro_Disciplina
def adicionar_livro_disciplina(id_livro, id_disciplina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Livro_Disciplina (ID_Livro, ID_Disciplina) VALUES (%s, %s)"
    valores = (id_livro, id_disciplina)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_livro_disciplina(id_livro, id_disciplina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Livro_Disciplina WHERE ID_Livro = %s AND ID_Disciplina = %s"
    valores = (id_livro, id_disciplina)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_livro_disciplina(id_livro, id_disciplina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Livro_Disciplina WHERE ID_Livro = %s AND ID_Disciplina = %s"
    valores = (id_livro, id_disciplina)
    cursor.execute(sql, valores)
    livro_disciplina = cursor.fetchone()
    cursor.close()
    conexao.close()
    return livro_disciplina

# Operações CRUD para a tabela Fornecedor
def adicionar_fornecedor(nome, telefone, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Fornecedor (Nome, Telefone, Email) VALUES (%s, %s, %s)"
    valores = (nome, telefone, email)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_fornecedor(id_fornecedor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Fornecedor WHERE ID_Fornecedor = %s"
    valores = (id_fornecedor,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_fornecedor(id_fornecedor, nome, telefone, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Fornecedor SET Nome = %s, Telefone = %s, Email = %s WHERE ID_Fornecedor = %s"
    valores = (nome, telefone, email, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_fornecedor(id_fornecedor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Fornecedor WHERE ID_Fornecedor = %s"
    valores = (id_fornecedor,)
    cursor.execute(sql, valores)
    fornecedor = cursor.fetchone()
    cursor.close()
    conexao.close()
    return fornecedor

# Operações CRUD para a tabela Emprestimo
def adicionar_emprestimo(data_emprestimo, data_devolucao, id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Emprestimo (DataEmprestimo, DataDevolucao, ID_Exemplar) VALUES (%s, %s, %s)"
    valores = (data_emprestimo, data_devolucao, id_exemplar)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_emprestimo(id_emprestimo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM Emprestimo WHERE ID_Emprestimo = %s"
    valores = (id_emprestimo,)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_emprestimo(id_emprestimo, data_emprestimo, data_devolucao, id_exemplar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE Emprestimo SET DataEmprestimo = %s, DataDevolucao = %s, ID_Exemplar = %s WHERE ID_Emprestimo = %s"
    valores = (data_emprestimo, data_devolucao, id_exemplar, id_emprestimo)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def pesquisar_emprestimo(id_emprestimo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM Emprestimo WHERE ID_Emprestimo = %s"
    valores = (id_emprestimo,)
    cursor.execute(sql, valores)
    emprestimo = cursor.fetchone()
    cursor.close()
    conexao.close()
    return emprestimo

# Manipulação em massa para Usuário
def adicionar_usuarios_em_massa(usuarios):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO Usuario (Nome, Email, Tipo) VALUES (%s, %s, %s)"
    valores = [(u['nome'], u['email'], u['tipo']) for u in usuarios]
    cursor.executemany(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# Função genérica de busca por substring para o Livro
def buscar_livros_por_titulo(substring):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = "SELECT * FROM Livro WHERE LOWER(Titulo) LIKE LOWER(%s)"
    cursor.execute(sql, (f"%{substring}%",))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

# Consulta 1: Agrupamento com COUNT e INNER JOIN
def livros_por_editora():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = """
    SELECT Editora.Nome, COUNT(Livro.ID_Livro) AS Total 
    FROM Editora
    INNER JOIN Livro ON Editora.ID_Editora = Livro.ID_Editora 
    GROUP BY Editora.Nome
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

# Consulta 2: LEFT JOIN e filtro com HAVING
def editoras_com_mais_de_5_livros():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = """
    SELECT Editora.Nome, COUNT(Livro.ID_Livro) AS Total 
    FROM Editora
    LEFT JOIN Livro ON Editora.ID_Editora = Livro.ID_Editora 
    GROUP BY Editora.Nome
    HAVING Total > 5
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

# Consulta usando ALL
# Função para consulta com ANY
def livros_mais_recentes_que_qualquer(ano):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = """
    SELECT * FROM Livro 
    WHERE AnoPublicacao > ANY (
        SELECT AnoPublicacao FROM Livro WHERE AnoPublicacao < %s
    )
    """
    cursor.execute(sql, (ano,))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

# Função para ordenação dinâmica
def listar_livros_ordenados(campo='Titulo', ordem='ASC'):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = f"SELECT * FROM Livro ORDER BY {campo} {ordem}"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

# Consulta usando ALL
def livros_mais_recentes_que_todos(ano):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = """
    SELECT * FROM Livro 
    WHERE AnoPublicacao > ALL (
        SELECT AnoPublicacao FROM Livro WHERE AnoPublicacao < %s
    )
    """
    cursor.execute(sql, (ano,))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados
