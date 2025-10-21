# Primeira página criada
# Necessário importar as bibliotecas necessárias para interagir com o banco de dados e o sistema de arquivos

# 1° passo: Importar o módulo 'sqlite3', que é a biblioteca padrão do Python para trabalhar com bancos de dados SQLite.
import sqlite3
# 2° passo: Importar o módulo 'os', que permite interagir com o sistema operacional, como verificar se um arquivo existe.
import os

DBFILENAME = "comidasdb.sqlite" # Nome do arquivo do banco de dados

def getconnection():
    """Abre uma conexão com o banco de dados SQLite."""

    # Estabelece comunicação com o arquivo no banco de dados
    conn = sqlite3.connect(DBFILENAME)
    conn.row_factory = sqlite3.Row # Permite acessar colunas por nome
    conn.execute("PRAGMA foreign_keys = ON") # Habilita suporte a chaves estrangeiras
    return conn
# 3° passo: Criar a função 'ensuredb' para garantir que o banco de dados e suas tabelas existam.
# Esta função verifica se o arquivo do banco de dados existe e, se não existir, cria o banco de dados e a tabela necessária.
def ensuredb():

    # Verifica se o arquivo do banco de dados já existe
    if not os.path.exists(DBFILENAME):
        scriptpath = os.path.join(os.path.dirname(__file__), "db_init.sql")
        if os.path.exists(scriptpath):
            with getconnection() as conn:
                with open(scriptpath, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
        else:
            raise FileNotFoundError("db_init.sql não encontrado. Coloque db_init.sql na mesma pasta.")