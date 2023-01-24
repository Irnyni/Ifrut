from time import sleep  # Importando o módulo do sqlite3 para manipularmos o banco de dados SQLITE3
from sqlite3 import Error
from datetime import date
from cores import Cores
import os
import sqlite3
from conexao import Conexao
from cliente import pessoa
from produtos import produto
banco='IFRUT'
c = Conexao()
c.connect()  
def criar_conexao(banco):
	"""Criando a conexão com o banco de dados Sqlite3."""
	# Variável conn inicializada para estabelecer a conexão com o banco
	conn = None
	# Tentará fazer a conexão com o banco de dados
	try:
		# Criando a conexão com o banco e salvando o objeto Connection na variável conn.
		conn = sqlite3.connect(banco)
		# Exibe a versão do Sqlite
		print(sqlite3.sqlite_version)
		# Sucesso na conexão. É retornado a conexão a quem chamou.
		return conn
	except Error as e:
		print(e)


def limpar():
    # Importando o módulo do sistema operacional (os) para usar instruções dele
    # Importando o módulo time para utilizar o método sleep que aguarda o 
    # tempo em segundos informando dentro do parênteses
    from time import sleep
    
    # Função para limpar a tela
    def screen_clear():
    # Para os sistemas operacionais: mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Para o sistema operacional windows
            _ = os.system('cls')
    # Aguarda 1 segundo para executar a próxima instrução
    sleep(1)
    # Chama a função de limpeza
    screen_clear()    




















