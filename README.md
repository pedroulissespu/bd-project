
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


