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

# Funções para a tabela Aluno
def adicionar_aluno_gui():
    id_usuario = entry_id_usuario_aluno.get()
    curso = entry_curso_aluno.get()
    matricula = entry_matricula_aluno.get()
    if id_usuario and curso and matricula:
        adicionar_aluno(int(id_usuario), curso, matricula)
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_aluno_gui():
    id_usuario = entry_id_usuario_aluno.get()
    if id_usuario:
        remover_aluno(int(id_usuario))
        messagebox.showinfo("Sucesso", "Aluno removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

def atualizar_aluno_gui():
    id_usuario = entry_id_usuario_aluno.get()
    curso = entry_curso_aluno.get()
    matricula = entry_matricula_aluno.get()
    if id_usuario and curso and matricula:
        atualizar_aluno(int(id_usuario), curso, matricula)
        messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_aluno_gui():
    id_usuario = entry_id_usuario_aluno.get()
    if id_usuario:
        aluno = pesquisar_aluno(int(id_usuario))
        if aluno:
            entry_curso_aluno.delete(0, tk.END)
            entry_curso_aluno.insert(0, aluno[1])  # Curso
            entry_matricula_aluno.delete(0, tk.END)
            entry_matricula_aluno.insert(0, aluno[2])  # Matrícula
        else:
            messagebox.showerror("Erro", "Aluno não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

# Funções para a tabela Professor
def adicionar_professor_gui():
    id_usuario = entry_id_usuario_professor.get()
    departamento = entry_departamento_professor.get()
    titulacao = entry_titulacao_professor.get()
    if id_usuario and departamento and titulacao:
        adicionar_professor(int(id_usuario), departamento, titulacao)
        messagebox.showinfo("Sucesso", "Professor adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_professor_gui():
    id_usuario = entry_id_usuario_professor.get()
    if id_usuario:
        remover_professor(int(id_usuario))
        messagebox.showinfo("Sucesso", "Professor removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

def atualizar_professor_gui():
    id_usuario = entry_id_usuario_professor.get()
    departamento = entry_departamento_professor.get()
    titulacao = entry_titulacao_professor.get()
    if id_usuario and departamento and titulacao:
        atualizar_professor(int(id_usuario), departamento, titulacao)
        messagebox.showinfo("Sucesso", "Professor atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_professor_gui():
    id_usuario = entry_id_usuario_professor.get()
    if id_usuario:
        professor = pesquisar_professor(int(id_usuario))
        if professor:
            entry_departamento_professor.delete(0, tk.END)
            entry_departamento_professor.insert(0, professor[1])  # Departamento
            entry_titulacao_professor.delete(0, tk.END)
            entry_titulacao_professor.insert(0, professor[2])  # Titulação
        else:
            messagebox.showerror("Erro", "Professor não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do usuário!")

# Funções para a tabela Categoria
def adicionar_categoria_gui():
    nome = entry_nome_categoria.get()
    if nome:
        adicionar_categoria(nome)
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha o campo nome!")

def remover_categoria_gui():
    id_categoria = entry_id_categoria.get()
    if id_categoria:
        remover_categoria(int(id_categoria))
        messagebox.showinfo("Sucesso", "Categoria removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID da categoria!")

def atualizar_categoria_gui():
    id_categoria = entry_id_categoria.get()
    nome = entry_nome_categoria.get()
    if id_categoria and nome:
        atualizar_categoria(int(id_categoria), nome)
        messagebox.showinfo("Sucesso", "Categoria atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_categoria_gui():
    id_categoria = entry_id_categoria.get()
    if id_categoria:
        categoria = pesquisar_categoria(int(id_categoria))
        if categoria:
            entry_nome_categoria.delete(0, tk.END)
            entry_nome_categoria.insert(0, categoria[1])  # Nome
        else:
            messagebox.showerror("Erro", "Categoria não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID da categoria!")

# Funções para a tabela Fornecedor
def adicionar_fornecedor_gui():
    nome = entry_nome_fornecedor.get()
    telefone = entry_telefone_fornecedor.get()
    email = entry_email_fornecedor.get()
    if nome and telefone and email:
        adicionar_fornecedor(nome, telefone, email)
        messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_fornecedor_gui():
    id_fornecedor = entry_id_fornecedor.get()
    if id_fornecedor:
        remover_fornecedor(int(id_fornecedor))
        messagebox.showinfo("Sucesso", "Fornecedor removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do fornecedor!")

def atualizar_fornecedor_gui():
    id_fornecedor = entry_id_fornecedor.get()
    nome = entry_nome_fornecedor.get()
    telefone = entry_telefone_fornecedor.get()
    email = entry_email_fornecedor.get()
    if id_fornecedor and nome and telefone and email:
        atualizar_fornecedor(int(id_fornecedor), nome, telefone, email)
        messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_fornecedor_gui():
    id_fornecedor = entry_id_fornecedor.get()
    if id_fornecedor:
        fornecedor = pesquisar_fornecedor(int(id_fornecedor))
        if fornecedor:
            entry_nome_fornecedor.delete(0, tk.END)
            entry_nome_fornecedor.insert(0, fornecedor[1])  # Nome
            entry_telefone_fornecedor.delete(0, tk.END)
            entry_telefone_fornecedor.insert(0, fornecedor[2])  # Telefone
            entry_email_fornecedor.delete(0, tk.END)
            entry_email_fornecedor.insert(0, fornecedor[3])  # Email
        else:
            messagebox.showerror("Erro", "Fornecedor não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do fornecedor!")

# Funções para a tabela Emprestimo
def adicionar_emprestimo_gui():
    data_emprestimo = entry_data_emprestimo.get()
    data_devolucao = entry_data_devolucao.get()
    id_exemplar = entry_id_exemplar_emprestimo.get()
    if data_emprestimo and data_devolucao and id_exemplar:
        adicionar_emprestimo(data_emprestimo, data_devolucao, int(id_exemplar))
        messagebox.showinfo("Sucesso", "Empréstimo adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_emprestimo_gui():
    id_emprestimo = entry_id_emprestimo.get()
    if id_emprestimo:
        remover_emprestimo(int(id_emprestimo))
        messagebox.showinfo("Sucesso", "Empréstimo removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do empréstimo!")

def atualizar_emprestimo_gui():
    id_emprestimo = entry_id_emprestimo.get()
    data_emprestimo = entry_data_emprestimo.get()
    data_devolucao = entry_data_devolucao.get()
    id_exemplar = entry_id_exemplar_emprestimo.get()
    if id_emprestimo and data_emprestimo and data_devolucao and id_exemplar:
        atualizar_emprestimo(int(id_emprestimo), data_emprestimo, data_devolucao, int(id_exemplar))
        messagebox.showinfo("Sucesso", "Empréstimo atualizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_emprestimo_gui():
    id_emprestimo = entry_id_emprestimo.get()
    if id_emprestimo:
        emprestimo = pesquisar_emprestimo(int(id_emprestimo))
        if emprestimo:
            entry_data_emprestimo.delete(0, tk.END)
            entry_data_emprestimo.insert(0, emprestimo[1])  # Data do Empréstimo
            entry_data_devolucao.delete(0, tk.END)
            entry_data_devolucao.insert(0, emprestimo[2])  # Data de Devolução
            entry_id_exemplar_emprestimo.delete(0, tk.END)
            entry_id_exemplar_emprestimo.insert(0, emprestimo[3])  # ID Exemplar
        else:
            messagebox.showerror("Erro", "Empréstimo não encontrado!")
    else:
        messagebox.showerror("Erro", "Informe o ID do empréstimo!")

# Funções para a tabela Livro_Autor
def adicionar_livro_autor_gui():
    id_livro = entry_id_livro_livro_autor.get()
    id_autor = entry_id_autor_livro_autor.get()
    if id_livro and id_autor:
        adicionar_livro_autor(int(id_livro), int(id_autor))
        messagebox.showinfo("Sucesso", "Relação Livro-Autor adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_livro_autor_gui():
    id_livro = entry_id_livro_livro_autor.get()
    id_autor = entry_id_autor_livro_autor.get()
    if id_livro and id_autor:
        remover_livro_autor(int(id_livro), int(id_autor))
        messagebox.showinfo("Sucesso", "Relação Livro-Autor removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e do autor!")

def pesquisar_livro_autor_gui():
    id_livro = entry_id_livro_livro_autor.get()
    id_autor = entry_id_autor_livro_autor.get()
    if id_livro and id_autor:
        livro_autor = pesquisar_livro_autor(int(id_livro), int(id_autor))
        if livro_autor:
            messagebox.showinfo("Sucesso", "Relação Livro-Autor encontrada!")
        else:
            messagebox.showerror("Erro", "Relação Livro-Autor não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e do autor!")

# Funções para a tabela Livro_Categoria
def adicionar_livro_categoria_gui():
    id_livro = entry_id_livro_livro_categoria.get()
    id_categoria = entry_id_categoria_livro_categoria.get()
    if id_livro and id_categoria:
        adicionar_livro_categoria(int(id_livro), int(id_categoria))
        messagebox.showinfo("Sucesso", "Relação Livro-Categoria adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_livro_categoria_gui():
    id_livro = entry_id_livro_livro_categoria.get()
    id_categoria = entry_id_categoria_livro_categoria.get()
    if id_livro and id_categoria:
        remover_livro_categoria(int(id_livro), int(id_categoria))
        messagebox.showinfo("Sucesso", "Relação Livro-Categoria removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e da categoria!")

def pesquisar_livro_categoria_gui():
    id_livro = entry_id_livro_livro_categoria.get()
    id_categoria = entry_id_categoria_livro_categoria.get()
    if id_livro and id_categoria:
        livro_categoria = pesquisar_livro_categoria(int(id_livro), int(id_categoria))
        if livro_categoria:
            messagebox.showinfo("Sucesso", "Relação Livro-Categoria encontrada!")
        else:
            messagebox.showerror("Erro", "Relação Livro-Categoria não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e da categoria!")

# Funções para a tabela Disciplina
def adicionar_disciplina_gui():
    nome = entry_nome_disciplina.get()
    curso = entry_curso_disciplina.get()
    if nome and curso:
        adicionar_disciplina(nome, curso)
        messagebox.showinfo("Sucesso", "Disciplina adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_disciplina_gui():
    id_disciplina = entry_id_disciplina.get()
    if id_disciplina:
        remover_disciplina(int(id_disciplina))
        messagebox.showinfo("Sucesso", "Disciplina removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID da disciplina!")

def atualizar_disciplina_gui():
    id_disciplina = entry_id_disciplina.get()
    nome = entry_nome_disciplina.get()
    curso = entry_curso_disciplina.get()
    if id_disciplina and nome and curso:
        atualizar_disciplina(int(id_disciplina), nome, curso)
        messagebox.showinfo("Sucesso", "Disciplina atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def pesquisar_disciplina_gui():
    id_disciplina = entry_id_disciplina.get()
    if id_disciplina:
        disciplina = pesquisar_disciplina(int(id_disciplina))
        if disciplina:
            entry_nome_disciplina.delete(0, tk.END)
            entry_nome_disciplina.insert(0, disciplina[1])  # Nome
            entry_curso_disciplina.delete(0, tk.END)
            entry_curso_disciplina.insert(0, disciplina[2])  # Curso
        else:
            messagebox.showerror("Erro", "Disciplina não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID da disciplina!")

# Funções para a tabela Livro_Disciplina
def adicionar_livro_disciplina_gui():
    id_livro = entry_id_livro_livro_disciplina.get()
    id_disciplina = entry_id_disciplina_livro_disciplina.get()
    if id_livro and id_disciplina:
        adicionar_livro_disciplina(int(id_livro), int(id_disciplina))
        messagebox.showinfo("Sucesso", "Relação Livro-Disciplina adicionada com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def remover_livro_disciplina_gui():
    id_livro = entry_id_livro_livro_disciplina.get()
    id_disciplina = entry_id_disciplina_livro_disciplina.get()
    if id_livro and id_disciplina:
        remover_livro_disciplina(int(id_livro), int(id_disciplina))
        messagebox.showinfo("Sucesso", "Relação Livro-Disciplina removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e da disciplina!")

def pesquisar_livro_disciplina_gui():
    id_livro = entry_id_livro_livro_disciplina.get()
    id_disciplina = entry_id_disciplina_livro_disciplina.get()
    if id_livro and id_disciplina:
        livro_disciplina = pesquisar_livro_disciplina(int(id_livro), int(id_disciplina))
        if livro_disciplina:
            messagebox.showinfo("Sucesso", "Relação Livro-Disciplina encontrada!")
        else:
            messagebox.showerror("Erro", "Relação Livro-Disciplina não encontrada!")
    else:
        messagebox.showerror("Erro", "Informe o ID do livro e da disciplina!")

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
aba_aluno = ttk.Frame(abas)
aba_professor = ttk.Frame(abas)
aba_categoria = ttk.Frame(abas)
aba_fornecedor = ttk.Frame(abas)
aba_emprestimo = ttk.Frame(abas)
aba_livro_autor = ttk.Frame(abas)
aba_livro_categoria = ttk.Frame(abas)
aba_disciplina = ttk.Frame(abas)
aba_livro_disciplina = ttk.Frame(abas)

abas.add(aba_usuario, text="Usuário")
abas.add(aba_livro, text="Livro")
abas.add(aba_editora, text="Editora")
abas.add(aba_autor, text="Autor")
abas.add(aba_exemplar, text="Exemplar")
abas.add(aba_reserva, text="Reserva")
abas.add(aba_aluno, text="Aluno")
abas.add(aba_professor, text="Professor")
abas.add(aba_categoria, text="Categoria")
abas.add(aba_fornecedor, text="Fornecedor")
abas.add(aba_emprestimo, text="Empréstimo")
abas.add(aba_livro_autor, text="Livro-Autor")
abas.add(aba_livro_categoria, text="Livro-Categoria")
abas.add(aba_disciplina, text="Disciplina")
abas.add(aba_livro_disciplina, text="Livro-Disciplina")

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

# Aba Aluno
tk.Label(aba_aluno, text="ID do Usuário:").grid(row=0, column=0)
entry_id_usuario_aluno = tk.Entry(aba_aluno)
entry_id_usuario_aluno.grid(row=0, column=1)

tk.Label(aba_aluno, text="Curso:").grid(row=1, column=0)
entry_curso_aluno = tk.Entry(aba_aluno)
entry_curso_aluno.grid(row=1, column=1)

tk.Label(aba_aluno, text="Matrícula:").grid(row=2, column=0)
entry_matricula_aluno = tk.Entry(aba_aluno)
entry_matricula_aluno.grid(row=2, column=1)

tk.Button(aba_aluno, text="Adicionar", command=adicionar_aluno_gui).grid(row=3, column=0)
tk.Button(aba_aluno, text="Remover", command=remover_aluno_gui).grid(row=3, column=1)
tk.Button(aba_aluno, text="Atualizar", command=atualizar_aluno_gui).grid(row=4, column=0)
tk.Button(aba_aluno, text="Pesquisar", command=pesquisar_aluno_gui).grid(row=4, column=1)

# Aba Professor
tk.Label(aba_professor, text="ID do Usuário:").grid(row=0, column=0)
entry_id_usuario_professor = tk.Entry(aba_professor)
entry_id_usuario_professor.grid(row=0, column=1)

tk.Label(aba_professor, text="Departamento:").grid(row=1, column=0)
entry_departamento_professor = tk.Entry(aba_professor)
entry_departamento_professor.grid(row=1, column=1)

tk.Label(aba_professor, text="Titulação:").grid(row=2, column=0)
entry_titulacao_professor = tk.Entry(aba_professor)
entry_titulacao_professor.grid(row=2, column=1)

tk.Button(aba_professor, text="Adicionar", command=adicionar_professor_gui).grid(row=3, column=0)
tk.Button(aba_professor, text="Remover", command=remover_professor_gui).grid(row=3, column=1)
tk.Button(aba_professor, text="Atualizar", command=atualizar_professor_gui).grid(row=4, column=0)
tk.Button(aba_professor, text="Pesquisar", command=pesquisar_professor_gui).grid(row=4, column=1)

# Aba Categoria
tk.Label(aba_categoria, text="ID da Categoria:").grid(row=0, column=0)
entry_id_categoria = tk.Entry(aba_categoria)
entry_id_categoria.grid(row=0, column=1)

tk.Label(aba_categoria, text="Nome:").grid(row=1, column=0)
entry_nome_categoria = tk.Entry(aba_categoria)
entry_nome_categoria.grid(row=1, column=1)

tk.Button(aba_categoria, text="Adicionar", command=adicionar_categoria_gui).grid(row=2, column=0)
tk.Button(aba_categoria, text="Remover", command=remover_categoria_gui).grid(row=2, column=1)
tk.Button(aba_categoria, text="Atualizar", command=atualizar_categoria_gui).grid(row=3, column=0)
tk.Button(aba_categoria, text="Pesquisar", command=pesquisar_categoria_gui).grid(row=3, column=1)

# Aba Fornecedor
tk.Label(aba_fornecedor, text="ID do Fornecedor:").grid(row=0, column=0)
entry_id_fornecedor = tk.Entry(aba_fornecedor)
entry_id_fornecedor.grid(row=0, column=1)

tk.Label(aba_fornecedor, text="Nome:").grid(row=1, column=0)
entry_nome_fornecedor = tk.Entry(aba_fornecedor)
entry_nome_fornecedor.grid(row=1, column=1)

tk.Label(aba_fornecedor, text="Telefone:").grid(row=2, column=0)
entry_telefone_fornecedor = tk.Entry(aba_fornecedor)
entry_telefone_fornecedor.grid(row=2, column=1)

tk.Label(aba_fornecedor, text="Email:").grid(row=3, column=0)
entry_email_fornecedor = tk.Entry(aba_fornecedor)
entry_email_fornecedor.grid(row=3, column=1)

tk.Button(aba_fornecedor, text="Adicionar", command=adicionar_fornecedor_gui).grid(row=4, column=0)
tk.Button(aba_fornecedor, text="Remover", command=remover_fornecedor_gui).grid(row=4, column=1)
tk.Button(aba_fornecedor, text="Atualizar", command=atualizar_fornecedor_gui).grid(row=5, column=0)
tk.Button(aba_fornecedor, text="Pesquisar", command=pesquisar_fornecedor_gui).grid(row=5, column=1)

# Aba Empréstimo
tk.Label(aba_emprestimo, text="ID do Empréstimo:").grid(row=0, column=0)
entry_id_emprestimo = tk.Entry(aba_emprestimo)
entry_id_emprestimo.grid(row=0, column=1)

tk.Label(aba_emprestimo, text="Data do Empréstimo:").grid(row=1, column=0)
entry_data_emprestimo = tk.Entry(aba_emprestimo)
entry_data_emprestimo.grid(row=1, column=1)

tk.Label(aba_emprestimo, text="Data de Devolução:").grid(row=2, column=0)
entry_data_devolucao = tk.Entry(aba_emprestimo)
entry_data_devolucao.grid(row=2, column=1)

tk.Label(aba_emprestimo, text="ID do Exemplar:").grid(row=3, column=0)
entry_id_exemplar_emprestimo = tk.Entry(aba_emprestimo)
entry_id_exemplar_emprestimo.grid(row=3, column=1)

tk.Button(aba_emprestimo, text="Adicionar", command=adicionar_emprestimo_gui).grid(row=4, column=0)
tk.Button(aba_emprestimo, text="Remover", command=remover_emprestimo_gui).grid(row=4, column=1)
tk.Button(aba_emprestimo, text="Atualizar", command=atualizar_emprestimo_gui).grid(row=5, column=0)
tk.Button(aba_emprestimo, text="Pesquisar", command=pesquisar_emprestimo_gui).grid(row=5, column=1)

# Aba Livro_Autor
tk.Label(aba_livro_autor, text="ID do Livro:").grid(row=0, column=0)
entry_id_livro_livro_autor = tk.Entry(aba_livro_autor)
entry_id_livro_livro_autor.grid(row=0, column=1)

tk.Label(aba_livro_autor, text="ID do Autor:").grid(row=1, column=0)
entry_id_autor_livro_autor = tk.Entry(aba_livro_autor)
entry_id_autor_livro_autor.grid(row=1, column=1)

tk.Button(aba_livro_autor, text="Adicionar", command=adicionar_livro_autor_gui).grid(row=2, column=0)
tk.Button(aba_livro_autor, text="Remover", command=remover_livro_autor_gui).grid(row=2, column=1)
tk.Button(aba_livro_autor, text="Pesquisar", command=pesquisar_livro_autor_gui).grid(row=3, column=0)

# Aba Livro_Categoria
tk.Label(aba_livro_categoria, text="ID do Livro:").grid(row=0, column=0)
entry_id_livro_livro_categoria = tk.Entry(aba_livro_categoria)
entry_id_livro_livro_categoria.grid(row=0, column=1)

tk.Label(aba_livro_categoria, text="ID da Categoria:").grid(row=1, column=0)
entry_id_categoria_livro_categoria = tk.Entry(aba_livro_categoria)
entry_id_categoria_livro_categoria.grid(row=1, column=1)

tk.Button(aba_livro_categoria, text="Adicionar", command=adicionar_livro_categoria_gui).grid(row=2, column=0)
tk.Button(aba_livro_categoria, text="Remover", command=remover_livro_categoria_gui).grid(row=2, column=1)
tk.Button(aba_livro_categoria, text="Pesquisar", command=pesquisar_livro_categoria_gui).grid(row=3, column=0)

# Aba Disciplina
tk.Label(aba_disciplina, text="ID da Disciplina:").grid(row=0, column=0)
entry_id_disciplina = tk.Entry(aba_disciplina)
entry_id_disciplina.grid(row=0, column=1)

tk.Label(aba_disciplina, text="Nome:").grid(row=1, column=0)
entry_nome_disciplina = tk.Entry(aba_disciplina)
entry_nome_disciplina.grid(row=1, column=1)

tk.Label(aba_disciplina, text="Curso:").grid(row=2, column=0)
entry_curso_disciplina = tk.Entry(aba_disciplina)
entry_curso_disciplina.grid(row=2, column=1)

tk.Button(aba_disciplina, text="Adicionar", command=adicionar_disciplina_gui).grid(row=3, column=0)
tk.Button(aba_disciplina, text="Remover", command=remover_disciplina_gui).grid(row=3, column=1)
tk.Button(aba_disciplina, text="Atualizar", command=atualizar_disciplina_gui).grid(row=4, column=0)
tk.Button(aba_disciplina, text="Pesquisar", command=pesquisar_disciplina_gui).grid(row=4, column=1)

# Aba Livro_Disciplina
tk.Label(aba_livro_disciplina, text="ID do Livro:").grid(row=0, column=0)
entry_id_livro_livro_disciplina = tk.Entry(aba_livro_disciplina)
entry_id_livro_livro_disciplina.grid(row=0, column=1)

tk.Label(aba_livro_disciplina, text="ID da Disciplina:").grid(row=1, column=0)
entry_id_disciplina_livro_disciplina = tk.Entry(aba_livro_disciplina)
entry_id_disciplina_livro_disciplina.grid(row=1, column=1)

tk.Button(aba_livro_disciplina, text="Adicionar", command=adicionar_livro_disciplina_gui).grid(row=2, column=0)
tk.Button(aba_livro_disciplina, text="Remover", command=remover_livro_disciplina_gui).grid(row=2, column=1)
tk.Button(aba_livro_disciplina, text="Pesquisar", command=pesquisar_livro_disciplina_gui).grid(row=3, column=0)

aba_consultas = ttk.Frame(abas)
abas.add(aba_consultas, text="Consultas Avançadas")

# Treeview para exibir resultados
tree = ttk.Treeview(aba_consultas, columns=("ID", "Título", "Ano", "Editora"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Título", text="Título")
tree.heading("Ano", text="Ano")
tree.heading("Editora", text="Editora")
tree.grid(row=4, column=0, columnspan=4, sticky="nsew")

def exibir_resultados(dados):
    for item in tree.get_children():
        tree.delete(item)
    for linha in dados:
        tree.insert("", "end", values=linha)

# Busca por substring
tk.Label(aba_consultas, text="Buscar Livros (Título):").grid(row=0, column=0)
entry_substring = tk.Entry(aba_consultas)
entry_substring.grid(row=0, column=1)

def buscar_substring_gui():
    substring = entry_substring.get()
    resultados = buscar_livros_por_titulo(substring)  # Função CRUD já implementada
    # Exibir resultados no Treeview (implementar função de exibição)
    exibir_resultados(resultados)

tk.Button(aba_consultas, text="Buscar", command=buscar_substring_gui).grid(row=0, column=2)

# Ordenação dinâmica
tk.Label(aba_consultas, text="Ordenar Livros por:").grid(row=1, column=0)
campo_ordenacao = ttk.Combobox(aba_consultas, values=["Titulo", "AnoPublicacao"])
campo_ordenacao.grid(row=1, column=1)
ordem_ordenacao = ttk.Combobox(aba_consultas, values=["ASC", "DESC"])
ordem_ordenacao.grid(row=1, column=2)

def ordenar_gui():
    campo = campo_ordenacao.get()
    ordem = ordem_ordenacao.get()
    resultados = listar_livros_ordenados(campo, ordem)  # Função CRUD parametrizada
    exibir_resultados(resultados)

tk.Button(aba_consultas, text="Ordenar", command=ordenar_gui).grid(row=1, column=3)

# Consultas com ANY/ALL
tk.Label(aba_consultas, text="Filtrar Livros (Ano >):").grid(row=2, column=0)
entry_ano_filtro = tk.Entry(aba_consultas)
entry_ano_filtro.grid(row=2, column=1)
quantificador = ttk.Combobox(aba_consultas, values=["ANY", "ALL"])
quantificador.grid(row=2, column=2)

def filtrar_quantificador_gui():
    ano = int(entry_ano_filtro.get())
    opcao = quantificador.get()
    if opcao == "ANY":
        resultados = livros_mais_recentes_que_qualquer(ano)  # Função CRUD com ANY
    else:
        resultados = livros_mais_recentes_que_todos(ano)  # Função CRUD com ALL
    exibir_resultados(resultados)

tk.Button(aba_consultas, text="Filtrar", command=filtrar_quantificador_gui).grid(row=2, column=3)

# Iniciar a interface gráfica
janela.mainloop()
