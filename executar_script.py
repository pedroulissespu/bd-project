import re

import mysql.connector

gatilho = """
CREATE TRIGGER atualizar_data_devolucao
BEFORE INSERT ON Emprestimo
FOR EACH ROW
BEGIN
    SET NEW.DataDevolucao = DATE_ADD(NEW.DataEmprestimo, INTERVAL 14 DAY);
END;
"""

# Função para ler o arquivo SQL
def ler_script_sql(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Função para dividir o script SQL em comandos individuais
def dividir_comandos_sql(script):
    # Usa regex para separar comandos, respeitando blocos BEGIN ... END
    comandos = re.split(r';(?=(?:[^\'"]|\'[^\']*\'|"[^"]*")*$)', script)
    comandos = [comando.strip() for comando in comandos if comando.strip()]
    return comandos

# Função para executar o script SQL
def executar_script_sql(script):
    conexao = None  # Inicializa a variável conexao como None
    try:
        # Conectar ao MySQL
        conexao = mysql.connector.connect(
            host="localhost",  # Endereço do servidor MySQL
            user="root",       # Usuário do MySQL
            password="root",  # Senha do MySQL
        )
        cursor = conexao.cursor()

        # Dividir o script em comandos individuais
        comandos = dividir_comandos_sql(script)

        # Executar cada comando individualmente
        for comando in comandos:
            try:
                cursor.execute(comando)
                print(f"Comando executado com sucesso: {comando[:50]}...")  # Exibe os primeiros 50 caracteres do comando
            except mysql.connector.Error as erro:
                print(f"Erro ao executar o comando: {comando[:50]}...")
                print(f"Detalhes do erro: {erro}")


        # Executar a criação do trigger/gatilho
        try:
            cursor.execute(gatilho)
            print("Gatilho criado com sucesso")
        except mysql.connector.Error as erro:
            print(f"Erro ao executar o gatilho:")
            print(f"Detalhes do erro: {erro}")

        # Confirmar as alterações
        conexao.commit()

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
    finally:
        # Fechar a conexão se ela foi estabelecida
        if conexao is not None and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada.")

# Caminho para o arquivo SQL
caminho_script_sql = "script.sql"

# Ler o script SQL
script_sql = ler_script_sql(caminho_script_sql)

# Executar o script SQL
executar_script_sql(script_sql)
