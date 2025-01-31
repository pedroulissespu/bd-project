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
