
# Sistema Gerenciador de Biblioteca - Projeto Final de Banco de Dados

Este projeto é uma aplicação Python com interface gráfica para gerenciar um sistema de biblioteca, utilizando MySQL como banco de dados.

## Índice

- [Sistema Gerenciador de Biblioteca - Projeto Final de Banco de Dados](#sistema-gerenciador-de-biblioteca---projeto-final-de-banco-de-dados)
  - [Equipe](#equipe)
  - [Requisitos do Sistema](#requisitos-do-sistema)
  - [Instalação](#instalação)
  - [Solução de Problemas Frequentes](#solução-de-problemas-frequentes)
  - [Preparação para executar](#preparação-para-executar)
  - [Explicação dos Arquivos e Estrutura do Projeto](#explicação-dos-arquivos-e-estrutura-do-projeto)
    - [`script.sql`](#1-scriptsql)
    - [`executar_script.py`](#2-executar_scriptpy)
    - [`crud.py`](#3-crudpy)
    - [`main.py`](#4-mainpy)
    - [`requirements.txt`](#5-requirementstxt)
    - [`README.md`](#6-readmemd)
  - [Como os Arquivos se Relacionam](#como-os-arquivos-se-relacionam)
  - [Como executar](#como-executar)
  - [Demonstração](#demonstração)
    - [Adicionar](#adicionar)
    - [Remover](#remover)
    - [Atualizar](#atualizar)
    - [Pesquisar](#pesquisar)
  - [Documentação](#documentação)
    - [Aba Usuário](#aba-usuário)
    - [Aba Livro](#aba-livro)
    - [Aba Editora](#aba-editora)
    - [Aba Autor](#aba-autor)
    - [Aba Exemplar](#aba-exemplar)
    - [Aba Reserva](#aba-reserva)
    - [Aba Aluno](#aba-aluno)
    - [Aba Professor](#aba-professor)
    - [Aba Categoria](#aba-categoria)
    - [Aba Fornecedor](#aba-fornecedor)
    - [Aba Empréstimo](#aba-empréstimo)
    - [Aba Livro_Autor](#aba-livro_autor)
    - [Aba Livro_Categoria](#aba-livro_categoria)
    - [Aba Disciplina](#aba-disciplina)
    - [Aba Livro_Disciplina](#aba-livro_disciplina)
  - [Exemplos](#exemplos)
    - [Adicionar um Novo Livro](#adicionar-um-novo-livro)
    - [Reservar um Exemplar](#reservar-um-exemplar)
    - [Adicionar um Novo Autor](#adicionar-um-novo-autor)
    - [Emprestar um Exemplar](#emprestar-um-exemplar)
  - [Observações](#observações)
  - [Contribuição](#contribuição)
  - [Contato](#contato)
  - [Agradecimentos](#agradecimentos)
  - [Referências](#referências)
  - [Licença](#licença)

## Equipe

- [Pedro Ulisses Pereira Castro Maia](https://github.com/pedroulissespu)
- [Larissa Kelly Dantas Batista](https://github.com/larikelly)
- [Andrei Carvalho Torres Portugal](https://github.com/AndreiPortugal)

## Requisitos do Sistema

- **Python**: Versão 3.12 ou superior.
- **MySQL**: Versão 8.0 ou superior.
- **Bibliotecas Python**: Verifique o arquivo `requirements.txt` para todas as dependências necessárias.
- **Sistema Operacional**: Compatível com Windows, Linux e macOS.

## Instalação

1. **Instale o MySQL**:
   - Se você não tem o MySQL instalado, siga as instruções no [site oficial do MySQL](https://dev.mysql.com/doc/refman/8.0/en/installing.html) para instalar o MySQL.
   - Se estiver usando Docker, execute o seguinte comando para rodar o MySQL:
     ```bash
     docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
     ```

2. **Instale o Python**:
   - Certifique-se de ter o Python 3.12 ou superior instalado. Você pode baixá-lo no [site oficial do Python](https://www.python.org/downloads/).

3. **Instale as dependências**:
   - Execute o seguinte comando para instalar as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```

4. **Execute o script de criação do banco de dados**:
   - Execute o script `executar_script.py` para criar o banco de dados e as tabelas:
     ```bash
     python executar_script.py
     ```

5. **Execute a aplicação**:
   - Para iniciar a interface gráfica, execute:
     ```bash
     python main.py
     ```
     
## Solução de Problemas Frequentes

- **Erro ao conectar ao MySQL**:
  - Verifique se o MySQL está rodando e se o usuário e senha estão corretos.
  - Certifique-se de que o MySQL está configurado para aceitar conexões externas, se necessário.

- **Erro ao instalar dependências**:
  - Certifique-se de que o Python está instalado corretamente e que o `pip` está atualizado.
  - Se o erro persistir, tente instalar as dependências manualmente:
    ```bash
    pip install mysql-connector-python tkinter
    ```

- **Erro ao executar o script SQL**:
  - Verifique se o arquivo `script.sql` está no diretório correto e se o MySQL está rodando.

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
## Explicação dos Arquivos e Estrutura do Projeto

Aqui está uma breve explicação de cada arquivo presente no projeto e sua função:

## 1. `script.sql`
**Descrição:** Contém o script SQL para criar o banco de dados `Biblioteca` e todas as suas tabelas, incluindo as relações entre elas.

**Função:**
- Cria o banco de dados `Biblioteca`.
- Define as tabelas: `Usuario`, `Aluno`, `Professor`, `Editora`, `Livro`, `Autor`, `Livro_Autor`, `Categoria`, `Livro_Categoria`, `Disciplina`, `Livro_Disciplina`, `Fornecedor`, `Exemplar`, `Reserva` e `Emprestimo`.
- Define as chaves primárias, estrangeiras e relacionamentos entre as tabelas.

**Uso:** Este script é executado automaticamente pelo arquivo `executar_script.py` para configurar o banco de dados.

---

## 2. `executar_script.py`
**Descrição:** Arquivo Python responsável por executar o script SQL (`script.sql`) para criar o banco de dados e suas tabelas.

**Função:**
- Conecta ao MySQL.
- Lê o arquivo `script.sql` e executa os comandos SQL para criar o banco de dados e as tabelas.
- Cria um gatilho (*trigger*) que define automaticamente a data de devolução de um empréstimo como 14 dias após a data do empréstimo.

**Uso:** Deve ser executado uma vez para configurar o banco de dados antes de rodar a aplicação principal.

---

## 3. `crud.py`
**Descrição:** Contém as funções CRUD (*Create, Read, Update, Delete*) para interagir com o banco de dados.

**Função:**
- Define funções para adicionar, remover, atualizar e pesquisar registros em todas as tabelas do banco de dados.
- Cada função se conecta ao banco de dados, executa a operação necessária e fecha a conexão.

**Uso:** Este arquivo é importado pelo `main.py` para realizar as operações de banco de dados a partir da interface gráfica.

---

## 4. `main.py`
**Descrição:** Arquivo principal da aplicação, que contém a interface gráfica do sistema de biblioteca.

**Função:**
- Cria uma interface gráfica usando a biblioteca `tkinter`.
- Permite ao usuário interagir com o banco de dados através de abas para cada tabela.
- Cada aba contém campos para adicionar, remover, atualizar e pesquisar registros.

**Uso:** Este arquivo deve ser executado para iniciar a aplicação e interagir com o sistema de biblioteca.

---

## 5. `requirements.txt`
**Descrição:** Lista as dependências necessárias para rodar o projeto.

**Função:**
- Especifica as bibliotecas Python necessárias, como `mysql-connector-python` para conectar ao MySQL e `tkinter` para a interface gráfica.

**Uso:** Execute `pip install -r requirements.txt` para instalar todas as dependências necessárias.

---

## 6. `README.md`
**Descrição:** Contém a documentação do projeto.

**Função:**
- Explica como configurar e executar o projeto.
- Documenta cada aba da interface gráfica e os campos que precisam ser preenchidos.
- Fornece exemplos de uso e observações importantes.

**Uso:** Serve como guia para quem está utilizando ou revisando o projeto.

---

## Como os Arquivos se Relacionam

### **Configuração do Banco de Dados:**
- O `executar_script.py` executa o `script.sql` para criar o banco de dados e as tabelas.

### **Operações de Banco de Dados:**
- O `crud.py` contém as funções que realizam as operações CRUD no banco de dados.

### **Interface Gráfica:**
- O `main.py` usa as funções do `crud.py` para permitir que o usuário interaja com o banco de dados através de uma interface gráfica.

### **Dependências:**
- O `requirements.txt` garante que todas as bibliotecas necessárias estejam instaladas para rodar o projeto.

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

## Contribuição

Se você quiser contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção de bug:
   ```bash
   git checkout -b minha-feature
3. Faça as alterações necessárias e commit:
   ```bash
   git commit -m "Adicionando nova funcionalidade"
4. Envie as alterações para o repositório remoto:
   ```bash
   git push origin minha-feature
5. Abra um Pull Request no GitHub.

## Contato

Em caso de dúvidas ou problemas, entre em contato com a equipe do projeto:

- **Pedro Ulisses Pereira Castro Maia**: [pedroulissespu](https://github.com/pedroulissespu)
- **Larissa Kelly Dantas Batista**: [larikelly](https://github.com/larikelly)
- **Andrei Carvalho Torres Portugal**: [AndreiPortugal](https://github.com/AndreiPortugal)

## Agradecimentos

Agradecemos aos seguintes recursos e pessoas que ajudaram no desenvolvimento deste projeto:

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [**Pedro Ulisses Pereira Castro Maia**](https://github.com/pedroulissespu)
- [**Larissa Kelly Dantas Batista**](https://github.com/larikelly)
- [**Andrei Carvalho Torres Portugal**](https://github.com/AndreiPortugal)

## Referências

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Tkinter Tutorial](https://realpython.com/python-gui-tkinter/)
- [Python MySQL Tutorial](https://pynative.com/python-mysql-tutorial/)

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/pedroulissespu/bd-project/blob/main/LICENSE) para mais detalhes.
