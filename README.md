
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
- Segue o vídeo demonstrando a criação :

### Remover
- Para criar qualquer entidade no Sistema, só precisa preencher todos os campos obrigatórios, depois de preencher os campos clicar em adicionar e vai aparecer uma janela confirmando a criação daquela entidade.
- Segue o vídeo demonstrando a criação :

### Atualizar
- Para criar qualquer entidade no Sistema, só precisa preencher todos os campos obrigatórios, depois de preencher os campos clicar em adicionar e vai aparecer uma janela confirmando a criação daquela entidade.
- Segue o vídeo demonstrando a criação :

### Pesquisar
- Para criar qualquer entidade no Sistema, só precisa preencher todos os campos obrigatórios, depois de preencher os campos clicar em adicionar e vai aparecer uma janela confirmando a criação daquela entidade.
- Segue o vídeo demonstrando a criação :


