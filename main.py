import tkinter as tk
from tkinter import ttk, messagebox
from crud import *

# Funções CRUD para a interface gráfica

# Funções para a tabela Usuario
def adicionar_usuario_gui():
    nome = entry_nome_usuario.get()
    email = entry_email_usuario.get()
    tipo = entry_tipo_usuario.get()
    if nome and email and tipo:
        adicionar_usuario(nome, email, tipo)
        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_usuario_gui():
    id_usuario = entry_id_usuario.get()
    if id_usuario:
        remover_usuario(int(id_usuario))
        messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

def atualizar_usuario_gui():
    id_usuario = entry_id_usuario.get()
    nome = entry_nome_usuario.get()
    email = entry_email_usuario.get()
    tipo = entry_tipo_usuario.get()
    if id_usuario and nome and email and tipo:
        atualizar_usuario(int(id_usuario), nome, email, tipo)
        messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_usuario_gui():
    id_usuario = entry_id_usuario.get()
    if id_usuario:
        usuario = pesquisar_usuario(int(id_usuario))
        if usuario:
            entry_nome_usuario.delete(0, tk.END)
            entry_nome_usuario.insert(0, usuario[1])  # Nome
            entry_email_usuario.delete(0, tk.END)
            entry_email_usuario.insert(0, usuario[2])  # Email
            entry_tipo_usuario.delete(0, tk.END)
            entry_tipo_usuario.insert(0, usuario[3])  # Tipo
        else:
            messagebox.showerror("Erro", "Usuário não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

# Funções para a tabela Livro
def adicionar_livro_gui():
    titulo = entry_titulo_livro.get()
    ano = entry_ano_livro.get()
    editora = entry_editora_livro.get()
    if titulo and ano and editora:
        adicionar_livro(titulo, int(ano), int(editora))
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_livro_gui():
    id_livro = entry_id_livro.get()
    if id_livro:
        remover_livro(int(id_livro))
        messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro!")

def atualizar_livro_gui():
    id_livro = entry_id_livro.get()
    titulo = entry_titulo_livro.get()
    ano = entry_ano_livro.get()
    editora = entry_editora_livro.get()
    if id_livro and titulo and ano and editora:
        atualizar_livro(int(id_livro), titulo, int(ano), int(editora))
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_livro_gui():
    id_livro = entry_id_livro.get()
    if id_livro:
        livro = pesquisar_livro(int(id_livro))
        if livro:
            entry_titulo_livro.delete(0, tk.END)
            entry_titulo_livro.insert(0, livro[1])  # Título
            entry_ano_livro.delete(0, tk.END)
            entry_ano_livro.insert(0, livro[2])  # Ano de Publicação
            entry_editora_livro.delete(0, tk.END)
            entry_editora_livro.insert(0, livro[3])  # ID da Editora
        else:
            messagebox.showerror("Erro", "Livro não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro!")

# Funções para a tabela Editora
def adicionar_editora_gui():
    nome = entry_nome_editora.get()
    cidade = entry_cidade_editora.get()
    if nome and cidade:
        adicionar_editora(nome, cidade)
        messagebox.showinfo("Sucesso", "Editora adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_editora_gui():
    id_editora = entry_id_editora.get()
    if id_editora:
        remover_editora(int(id_editora))
        messagebox.showinfo("Sucesso", "Editora removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID da editora!")

def atualizar_editora_gui():
    id_editora = entry_id_editora.get()
    nome = entry_nome_editora.get()
    cidade = entry_cidade_editora.get()
    if id_editora and nome and cidade:
        atualizar_editora(int(id_editora), nome, cidade)
        messagebox.showinfo("Sucesso", "Editora atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_editora_gui():
    id_editora = entry_id_editora.get()
    if id_editora:
        editora = pesquisar_editora(int(id_editora))
        if editora:
            entry_nome_editora.delete(0, tk.END)
            entry_nome_editora.insert(0, editora[1])  # Nome
            entry_cidade_editora.delete(0, tk.END)
            entry_cidade_editora.insert(0, editora[2])  # Cidade
        else:
            messagebox.showerror("Erro", "Editora não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID da editora!")

# Funções para a tabela Autor
def adicionar_autor_gui():
    nome = entry_nome_autor.get()
    if nome:
        adicionar_autor(nome)
        messagebox.showinfo("Sucesso", "Autor adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha o campo nome!")

def remover_autor_gui():
    id_autor = entry_id_autor.get()
    if id_autor:
        remover_autor(int(id_autor))
        messagebox.showinfo("Sucesso", "Autor removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do autor!")

def atualizar_autor_gui():
    id_autor = entry_id_autor.get()
    nome = entry_nome_autor.get()
    if id_autor and nome:
        atualizar_autor(int(id_autor), nome)
        messagebox.showinfo("Sucesso", "Autor atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_autor_gui():
    id_autor = entry_id_autor.get()
    if id_autor:
        autor = pesquisar_autor(int(id_autor))
        if autor:
            entry_nome_autor.delete(0, tk.END)
            entry_nome_autor.insert(0, autor[1])  # Nome
        else:
            messagebox.showerror("Erro", "Autor não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do autor!")

# Funções para a tabela Exemplar
def adicionar_exemplar_gui():
    localizacao = entry_localizacao_exemplar.get()
    id_livro = entry_id_livro_exemplar.get()
    id_fornecedor = entry_id_fornecedor_exemplar.get()
    if localizacao and id_livro and id_fornecedor:
        adicionar_exemplar(localizacao, int(id_livro), int(id_fornecedor))
        messagebox.showinfo("Sucesso", "Exemplar adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_exemplar_gui():
    id_exemplar = entry_id_exemplar.get()
    if id_exemplar:
        remover_exemplar(int(id_exemplar))
        messagebox.showinfo("Sucesso", "Exemplar removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do exemplar!")

def atualizar_exemplar_gui():
    id_exemplar = entry_id_exemplar.get()
    localizacao = entry_localizacao_exemplar.get()
    id_livro = entry_id_livro_exemplar.get()
    id_fornecedor = entry_id_fornecedor_exemplar.get()
    if id_exemplar and localizacao and id_livro and id_fornecedor:
        atualizar_exemplar(int(id_exemplar), localizacao, int(id_livro), int(id_fornecedor))
        messagebox.showinfo("Sucesso", "Exemplar atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_exemplar_gui():
    id_exemplar = entry_id_exemplar.get()
    if id_exemplar:
        exemplar = pesquisar_exemplar(int(id_exemplar))
        if exemplar:
            entry_localizacao_exemplar.delete(0, tk.END)
            entry_localizacao_exemplar.insert(0, exemplar[1])  # Localização
            entry_id_livro_exemplar.delete(0, tk.END)
            entry_id_livro_exemplar.insert(0, exemplar[2])  # ID Livro
            entry_id_fornecedor_exemplar.delete(0, tk.END)
            entry_id_fornecedor_exemplar.insert(0, exemplar[3])  # ID Fornecedor
        else:
            messagebox.showerror("Erro", "Exemplar não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do exemplar!")

# Funções para a tabela Reserva
def adicionar_reserva_gui():
    data_reserva = entry_data_reserva.get()
    id_usuario = entry_id_usuario_reserva.get()
    id_exemplar = entry_id_exemplar_reserva.get()
    if data_reserva and id_usuario and id_exemplar:
        adicionar_reserva(data_reserva, int(id_usuario), int(id_exemplar))
        messagebox.showinfo("Sucesso", "Reserva adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_reserva_gui():
    id_reserva = entry_id_reserva.get()
    if id_reserva:
        remover_reserva(int(id_reserva))
        messagebox.showinfo("Sucesso", "Reserva removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID da reserva!")

def atualizar_reserva_gui():
    id_reserva = entry_id_reserva.get()
    data_reserva = entry_data_reserva.get()
    id_usuario = entry_id_usuario_reserva.get()
    id_exemplar = entry_id_exemplar_reserva.get()
    if id_reserva and data_reserva and id_usuario and id_exemplar:
        atualizar_reserva(int(id_reserva), data_reserva, int(id_usuario), int(id_exemplar))
        messagebox.showinfo("Sucesso", "Reserva atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_reserva_gui():
    id_reserva = entry_id_reserva.get()
    if id_reserva:
        reserva = pesquisar_reserva(int(id_reserva))
        if reserva:
            entry_data_reserva.delete(0, tk.END)
            entry_data_reserva.insert(0, reserva[1])  # Data da Reserva
            entry_id_usuario_reserva.delete(0, tk.END)
            entry_id_usuario_reserva.insert(0, reserva[2])  # ID Usuário
            entry_id_exemplar_reserva.delete(0, tk.END)
            entry_id_exemplar_reserva.insert(0, reserva[3])  # ID Exemplar
        else:
            messagebox.showerror("Erro", "Reserva não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID da reserva!")

# Interface gráfica
janela = tk.Tk()
janela.title("Sistema de Biblioteca")

# Abas para cada tabela
abas = ttk.Notebook(janela)
aba_usuario = ttk.Frame(abas)
aba_livro = ttk.Frame(abas)
aba_editora = ttk.Frame(abas)
aba_autor = ttk.Frame(abas)
aba_exemplar = ttk.Frame(abas)
aba_reserva = ttk.Frame(abas)

abas.add(aba_usuario, text="Usuário")
abas.add(aba_livro, text="Livro")
abas.add(aba_editora, text="Editora")
abas.add(aba_autor, text="Autor")
abas.add(aba_exemplar, text="Exemplar")
abas.add(aba_reserva, text="Reserva")

abas.pack(expand=1, fill="both")

# Aba Usuário
tk.Label(aba_usuario, text="ID do Usuário:").grid(row=0, column=0)
entry_id_usuario = tk.Entry(aba_usuario)
entry_id_usuario.grid(row=0, column=1)

tk.Label(aba_usuario, text="Nome:").grid(row=1, column=0)
entry_nome_usuario = tk.Entry(aba_usuario)
entry_nome_usuario.grid(row=1, column=1)

tk.Label(aba_usuario, text="Email:").grid(row=2, column=0)
entry_email_usuario = tk.Entry(aba_usuario)
entry_email_usuario.grid(row=2, column=1)

tk.Label(aba_usuario, text="Tipo:").grid(row=3, column=0)
entry_tipo_usuario = tk.Entry(aba_usuario)
entry_tipo_usuario.grid(row=3, column=1)

tk.Button(aba_usuario, text="Adicionar", command=adicionar_usuario_gui).grid(row=4, column=0)
tk.Button(aba_usuario, text="Remover", command=remover_usuario_gui).grid(row=4, column=1)
tk.Button(aba_usuario, text="Atualizar", command=atualizar_usuario_gui).grid(row=5, column=0)
tk.Button(aba_usuario, text="Pesquisar", command=pesquisar_usuario_gui).grid(row=5, column=1)

# Aba Livro
tk.Label(aba_livro, text="ID do Livro:").grid(row=0, column=0)
entry_id_livro = tk.Entry(aba_livro)
entry_id_livro.grid(row=0, column=1)

tk.Label(aba_livro, text="Título:").grid(row=1, column=0)
entry_titulo_livro = tk.Entry(aba_livro)
entry_titulo_livro.grid(row=1, column=1)

tk.Label(aba_livro, text="Ano de Publicação:").grid(row=2, column=0)
entry_ano_livro = tk.Entry(aba_livro)
entry_ano_livro.grid(row=2, column=1)

tk.Label(aba_livro, text="ID da Editora:").grid(row=3, column=0)
entry_editora_livro = tk.Entry(aba_livro)
entry_editora_livro.grid(row=3, column=1)

tk.Button(aba_livro, text="Adicionar", command=adicionar_livro_gui).grid(row=4, column=0)
tk.Button(aba_livro, text="Remover", command=remover_livro_gui).grid(row=4, column=1)
tk.Button(aba_livro, text="Atualizar", command=atualizar_livro_gui).grid(row=5, column=0)
tk.Button(aba_livro, text="Pesquisar", command=pesquisar_livro_gui).grid(row=5, column=1)

# Aba Editora
tk.Label(aba_editora, text="ID da Editora:").grid(row=0, column=0)
entry_id_editora = tk.Entry(aba_editora)
entry_id_editora.grid(row=0, column=1)

tk.Label(aba_editora, text="Nome:").grid(row=1, column=0)
entry_nome_editora = tk.Entry(aba_editora)
entry_nome_editora.grid(row=1, column=1)

tk.Label(aba_editora, text="Cidade:").grid(row=2, column=0)
entry_cidade_editora = tk.Entry(aba_editora)
entry_cidade_editora.grid(row=2, column=1)

tk.Button(aba_editora, text="Adicionar", command=adicionar_editora_gui).grid(row=3, column=0)
tk.Button(aba_editora, text="Remover", command=remover_editora_gui).grid(row=3, column=1)
tk.Button(aba_editora, text="Atualizar", command=atualizar_editora_gui).grid(row=4, column=0)
tk.Button(aba_editora, text="Pesquisar", command=pesquisar_editora_gui).grid(row=4, column=1)

# Aba Autor
tk.Label(aba_autor, text="ID do Autor:").grid(row=0, column=0)
entry_id_autor = tk.Entry(aba_autor)
entry_id_autor.grid(row=0, column=1)

tk.Label(aba_autor, text="Nome:").grid(row=1, column=0)
entry_nome_autor = tk.Entry(aba_autor)
entry_nome_autor.grid(row=1, column=1)

tk.Button(aba_autor, text="Adicionar", command=adicionar_autor_gui).grid(row=2, column=0)
tk.Button(aba_autor, text="Remover", command=remover_autor_gui).grid(row=2, column=1)
tk.Button(aba_autor, text="Atualizar", command=atualizar_autor_gui).grid(row=3, column=0)
tk.Button(aba_autor, text="Pesquisar", command=pesquisar_autor_gui).grid(row=3, column=1)

# Aba Exemplar
tk.Label(aba_exemplar, text="ID do Exemplar:").grid(row=0, column=0)
entry_id_exemplar = tk.Entry(aba_exemplar)
entry_id_exemplar.grid(row=0, column=1)

tk.Label(aba_exemplar, text="Localização:").grid(row=1, column=0)
entry_localizacao_exemplar = tk.Entry(aba_exemplar)
entry_localizacao_exemplar.grid(row=1, column=1)

tk.Label(aba_exemplar, text="ID do Livro:").grid(row=2, column=0)
entry_id_livro_exemplar = tk.Entry(aba_exemplar)
entry_id_livro_exemplar.grid(row=2, column=1)

tk.Label(aba_exemplar, text="ID do Fornecedor:").grid(row=3, column=0)
entry_id_fornecedor_exemplar = tk.Entry(aba_exemplar)
entry_id_fornecedor_exemplar.grid(row=3, column=1)

tk.Button(aba_exemplar, text="Adicionar", command=adicionar_exemplar_gui).grid(row=4, column=0)
tk.Button(aba_exemplar, text="Remover", command=remover_exemplar_gui).grid(row=4, column=1)
tk.Button(aba_exemplar, text="Atualizar", command=atualizar_exemplar_gui).grid(row=5, column=0)
tk.Button(aba_exemplar, text="Pesquisar", command=pesquisar_exemplar_gui).grid(row=5, column=1)

# Aba Reserva
tk.Label(aba_reserva, text="ID da Reserva:").grid(row=0, column=0)
entry_id_reserva = tk.Entry(aba_reserva)
entry_id_reserva.grid(row=0, column=1)

tk.Label(aba_reserva, text="Data da Reserva:").grid(row=1, column=0)
entry_data_reserva = tk.Entry(aba_reserva)
entry_data_reserva.grid(row=1, column=1)

tk.Label(aba_reserva, text="ID do Usuário:").grid(row=2, column=0)
entry_id_usuario_reserva = tk.Entry(aba_reserva)
entry_id_usuario_reserva.grid(row=2, column=1)

tk.Label(aba_reserva, text="ID do Exemplar:").grid(row=3, column=0)
entry_id_exemplar_reserva = tk.Entry(aba_reserva)
entry_id_exemplar_reserva.grid(row=3, column=1)

tk.Button(aba_reserva, text="Adicionar", command=adicionar_reserva_gui).grid(row=4, column=0)
tk.Button(aba_reserva, text="Remover", command=remover_reserva_gui).grid(row=4, column=1)
tk.Button(aba_reserva, text="Atualizar", command=atualizar_reserva_gui).grid(row=5, column=0)
tk.Button(aba_reserva, text="Pesquisar", command=pesquisar_reserva_gui).grid(row=5, column=1)

# Iniciar a interface gráfica
janela.mainloop()
