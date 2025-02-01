
# Sistema Gerenciador de Biblioteca - Projeto Final de Banco de Dados

Este projeto é uma aplicação Python com interface gráfica para gerenciar um sistema de biblioteca, utilizando MySQL como banco de dados.
## Equipe

- [Pedro Ulisses Pereira Castro Maia](https://github.com/pedroulissespu)
- [Larissa Kelly Dantas Batista](https://github.com/larikelly)
- [Andrei Carvalho Torres Portugal](https://github.com/AndreiPortugal)
## Preparação para executar

1. Tenha em sua máquina instalado o MySQL ou se não tiver instalado e use o Docker, tenha o Docker rodando o MySQL.
2. Crie um usuário e senha root(ou se quiser personalizar isso, vai ter que alterar o usuário e senha também nos arquivos executar_script.py e crud.py). Para editar a senha e o usuário vai estar presente na seguinte parte de código :
    ```python
        conexao = mysql.connector.connect(
            host="localhost",  # Endereço do servidor MySQL
            user="root",       # Usuário do MySQL
            password="root",  # Senha do MySQL
        )
    ```
   ou
    ```python
    return mysql.connector.connect(
        host="localhost",  # Endereço do servidor MySQL
        user="root",       # Usuário do MySQL
        password="root",  # Senha do MySQL
        database="Biblioteca"  # Nome do banco de dados
    )
    ``` 
3. Tenha o Python na versão 3.12 ou mais recente instalado em sua máquina.
4. Instale as dependências necessárias do projeto pelo requirements.txt. Executando o seguinte comando :
    ```shell
   pip install -r requirements.txt
   ```
5. Execute o script em python executar_script.py para criar o banco de dados, suas tabelas e o gatilho.
    ```shell
   python executar_script.py
   ```

## Como executar

1. Para executar o sistema só executar o arquivo em python main.py que possui a interface gráfica e com isso pode seguir para a parte de demonstração que vai demonstrar como funciona o sistema.
    ```shell
   python main.py
   ```
## Demonstração

### Adicionar
- Para criar qualquer entidade no Sistema, só precisa preencher todos os campos obrigatórios, depois de preencher os campos clicar em adicionar e vai aparecer uma janela confirmando a criação daquela entidade.
- Segue o vídeo demonstrando a criação : <br />
  ![Desktop-2025-02-01-4-58-38-PM_1](https://github.com/user-attachments/assets/908eb398-e3cd-45c5-9fb4-ef2ce808e65b)


### Remover
- Para remover qualquer entidade no Sistema, só precisa preencher o ID daquilo que deseja remover, depois de preencher o ID clicar em Remover e vai aparecer uma janela confirmando a remoção daquela entidade. Caso tente buscar pela entidade que removeu, vai aparecer que não existe mais !
- Segue o vídeo demonstrando a remoção : <br />
  ![Desktop-2025-02-01-4-59-26-PM_1](https://github.com/user-attachments/assets/5ed9d4a3-a0ea-4efa-b89f-66338adf4b56)


### Atualizar
- Para atualizar qualquer entidade no Sistema, só precisa preencher os campos que quer atualizar, depois de preencher os campos clicar em Atualizar e vai aparecer uma janela confirmando a atualização daquela entidade. Caso tente buscar pela entidade que atualizou, vai aparecer com os dados modificados !
- Segue o vídeo demonstrando a criação : <br />
  ![Desktop-2025-02-01-4-59-58-PM_1](https://github.com/user-attachments/assets/be6771b7-dcce-45b3-8474-b71aa3d55bde)

### Pesquisar
- Para pesquisar qualquer entidade no Sistema, só precisa preencher o ID daquilo que deseja pesquisar, depois de preencher o ID clicar em Pesquisar vai ser preenchido os campos com as informações da entidade com aquele ID.
- Segue o vídeo demonstrando a criação : <br />
  ![Desktop-2025-02-01-4-59-06-PM_1](https://github.com/user-attachments/assets/0358bde8-1c4e-42ed-bbd2-395089ee5ba2)

## Documentação

### Aba Usuário

- **ID do Usuário**: Identificador único do usuário (gerado automaticamente ao adicionar um novo usuário).
- **Nome**: Nome completo do usuário.
- **Email**: Endereço de e-mail do usuário.
- **Tipo**: Tipo de usuário (Aluno ou Professor).

### Aba Livro

- **ID do Livro**: Identificador único do livro (gerado automaticamente ao adicionar um novo livro).
- **Título**: Título do livro.
- **Ano de Publicação**: Ano em que o livro foi publicado.
- **ID da Editora**: Identificador da editora que publicou o livro.

### Aba Editora

- **ID da Editora**: Identificador único da editora (gerado automaticamente ao adicionar uma nova editora).
- **Nome**: Nome da editora.
- **Cidade**: Cidade onde a editora está localizada.

### Aba Autor

- **ID do Autor**: Identificador único do autor (gerado automaticamente ao adicionar um novo autor).
- **Nome**: Nome completo do autor.

### Aba Exemplar

- **ID do Exemplar**: Identificador único do exemplar (gerado automaticamente ao adicionar um novo exemplar).
- **Localização**: Localização física do exemplar na biblioteca.
- **ID do Livro**: Identificador do livro ao qual o exemplar pertence.
- **ID do Fornecedor**: Identificador do fornecedor que forneceu o exemplar.

### Aba Reserva

- **ID da Reserva**: Identificador único da reserva (gerado automaticamente ao adicionar uma nova reserva).
- **Data da Reserva**: Data em que a reserva foi feita.
- **ID do Usuário**: Identificador do usuário que fez a reserva.
- **ID do Exemplar**: Identificador do exemplar que foi reservado.

### Aba Aluno

- **ID do Usuário**: Identificador do usuário que é um aluno.
- **Curso**: Curso em que o aluno está matriculado.
- **Matrícula**: Número de matrícula do aluno.

### Aba Professor

- **ID do Usuário**: Identificador do usuário que é um professor.
- **Departamento**: Departamento ao qual o professor pertence.
- **Titulação**: Titulação acadêmica do professor.

### Aba Categoria

- **ID da Categoria**: Identificador único da categoria (gerado automaticamente ao adicionar uma nova categoria).
- **Nome**: Nome da categoria.

### Aba Fornecedor

- **ID do Fornecedor**: Identificador único do fornecedor (gerado automaticamente ao adicionar um novo fornecedor).
- **Nome**: Nome do fornecedor.
- **Telefone**: Número de telefone do fornecedor.
- **Email**: Endereço de e-mail do fornecedor.

### Aba Empréstimo

- **ID do Empréstimo**: Identificador único do empréstimo (gerado automaticamente ao adicionar um novo empréstimo).
- **Data do Empréstimo**: Data em que o empréstimo foi realizado.
- **Data de Devolução**: Data prevista para a devolução do exemplar.
- **ID do Exemplar**: Identificador do exemplar que foi emprestado.

### Aba Livro_Autor

- **ID do Livro**: Identificador do livro.
- **ID do Autor**: Identificador do autor.
- **Ação**: Adicionar, remover ou pesquisar a relação entre livro e autor.

### Aba Livro_Categoria

- **ID do Livro**: Identificador do livro.
- **ID da Categoria**: Identificador da categoria.
- **Ação**: Adicionar, remover ou pesquisar a relação entre livro e categoria.

### Aba Disciplina

- **ID da Disciplina**: Identificador único da disciplina (gerado automaticamente ao adicionar uma nova disciplina).
- **Nome**: Nome da disciplina.
- **Curso**: Curso ao qual a disciplina pertence.

### Aba Livro_Disciplina

- **ID do Livro**: Identificador do livro.
- **ID da Disciplina**: Identificador da disciplina.
- **Ação**: Adicionar, remover ou pesquisar a relação entre livro e disciplina.

### Exemplos

#### Adicionar um Novo Livro
- **Título**: "Dom Casmurro"
- **Ano de Publicação**: 1899
- **ID da Editora**: 1

#### Reservar um Exemplar
- **Data da Reserva**: 2023-10-01
- **ID do Usuário**: 2
- **ID do Exemplar**: 5

#### Adicionar um Novo Autor
- **Nome**: "Machado de Assis"

#### Emprestar um Exemplar
- **Data do Empréstimo**: 2023-10-01
- **Data de Devolução**: 2023-10-15
- **ID do Exemplar**: 5

### Observações
- Certifique-se de que os IDs fornecidos existam nas tabelas relacionadas.
- As datas devem ser inseridas no formato `YYYY-MM-DD`.
