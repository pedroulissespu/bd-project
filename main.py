import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",  # Endereço do MySQL (no Docker ou local)
            user="root",       # Usuário do MySQL
            password="root",  # Senha do MySQL
            database="Biblioteca"   # Nome do banco de dados
        )
        return conexao
    except Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Operações CRUD
def inserir_usuario(nome, email):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO Usuario (Nome, Email) VALUES (%s, %s)"
        valores = (nome, email)
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

def remover_usuario(id_usuario):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM Usuario WHERE ID_Usuario = %s"
        valores = (id_usuario,)
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao remover usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_usuario(id_usuario, nome, email):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE Usuario SET Nome = %s, Email = %s WHERE ID_Usuario = %s"
        valores = (nome, email, id_usuario)
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

def buscar_usuario(id_usuario):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM Usuario WHERE ID_Usuario = %s"
        valores = (id_usuario,)
        try:
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
            if usuario:
                messagebox.showinfo("Usuário Encontrado", f"Nome: {usuario['Nome']}\nEmail: {usuario['Email']}")
            else:
                messagebox.showinfo("Usuário Não Encontrado", "Nenhum usuário encontrado com o ID fornecido.")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao buscar usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

# Consultas Avançadas
def buscar_livro_por_titulo(substring):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM Livro WHERE LOWER(Titulo) LIKE LOWER(%s)"
        valores = (f"%{substring}%",)
        try:
            cursor.execute(sql, valores)
            livros = cursor.fetchall()
            if livros:
                resultado = "\n".join([f"Título: {livro['Titulo']}, Ano: {livro['Ano_Publicacao']}" for livro in livros])
                messagebox.showinfo("Livros Encontrados", resultado)
            else:
                messagebox.showinfo("Nenhum Livro Encontrado", "Nenhum livro encontrado com o título fornecido.")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao buscar livros: {e}")
        finally:
            cursor.close()
            conexao.close()

def livros_por_editora():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = """
        SELECT Editora.Nome AS Editora, COUNT(Livro.ID_Livro) AS Total_Livros
        FROM Livro
        JOIN Editora ON Livro.ID_Editora = Editora.ID_Editora
        GROUP BY Editora.Nome
        """
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            if resultados:
                resultado = "\n".join([f"Editora: {row['Editora']}, Livros: {row['Total_Livros']}" for row in resultados])
                messagebox.showinfo("Livros por Editora", resultado)
            else:
                messagebox.showinfo("Nenhum Resultado", "Nenhum resultado encontrado.")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao buscar livros por editora: {e}")
        finally:
            cursor.close()
            conexao.close()

# Interface Gráfica
def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    if nome and email:
        inserir_usuario(nome, email)
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

def buscar_usuario_interface():
    id_usuario = entry_id_usuario.get()
    if id_usuario:
        buscar_usuario(int(id_usuario))
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, insira o ID do usuário.")

def buscar_livro_interface():
    substring = entry_titulo_livro.get()
    if substring:
        buscar_livro_por_titulo(substring)
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, insira um título para buscar.")

# Configuração da Interface Gráfica
janela = tk.Tk()
janela.title("Sistema de Biblioteca")

# Campos de entrada para cadastro de usuário
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

label_email = tk.Label(janela, text="Email:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

botao_cadastrar = tk.Button(janela, text="Cadastrar Usuário", command=cadastrar_usuario)
botao_cadastrar.grid(row=2, column=0, columnspan=2)

# Campos de entrada para buscar usuário
label_id_usuario = tk.Label(janela, text="ID do Usuário:")
label_id_usuario.grid(row=3, column=0)
entry_id_usuario = tk.Entry(janela)
entry_id_usuario.grid(row=3, column=1)

botao_buscar_usuario = tk.Button(janela, text="Buscar Usuário", command=buscar_usuario_interface)
botao_buscar_usuario.grid(row=4, column=0, columnspan=2)

# Campos de entrada para buscar livro por título
label_titulo_livro = tk.Label(janela, text="Título do Livro:")
label_titulo_livro.grid(row=5, column=0)
entry_titulo_livro = tk.Entry(janela)
entry_titulo_livro.grid(row=5, column=1)

botao_buscar_livro = tk.Button(janela, text="Buscar Livro", command=buscar_livro_interface)
botao_buscar_livro.grid(row=6, column=0, columnspan=2)

# Botão para consulta avançada (livros por editora)
botao_livros_por_editora = tk.Button(janela, text="Livros por Editora", command=livros_por_editora)
botao_livros_por_editora.grid(row=7, column=0, columnspan=2)

# Iniciar a interface gráfica
janela.mainloop()
