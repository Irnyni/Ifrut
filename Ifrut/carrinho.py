from time import sleep  # Importando o módulo do sqlite3 para manipularmos o banco de dados SQLITE3
from sqlite3 import Error
from datetime import date
from cores import Cores
import os
import sqlite3
import schema
from conexao import Conexao
from cliente import pessoa
from produtos import produto
from vendedor import vendedor


def pesquisar(id):
          id=str(id)

          try:
              c = Conexao()
              c.connect()  
              c.execute("SELECT * FROM carrinho WHERE idclient like (?);",
                          ('%' + id + '%', ))
              resultado = c.fetchall()  
              print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\t\t\tCARRINHO DE PEDIDOS\n\n{Cores.ENDC}')                         
    
              if resultado: 
      #Mostrar itens do cliente-----------------------------------------------------
                  print(f"{Cores.BOLD}{Cores.Red}")
                  print(" {:<10} | {:<10} | {:<10} | {:<5} | {:<10} | {:<10}  ".format(
                      "CARRINHO","ID CLIENTE","IDPRODUTO","QTDE", "DESCRIÇAO","PREÇO UN")) # titulo dos dados apresentados -------
                  print( 65 * '*' + f"{Cores.ENDC} ")
    
      #mostrar cada item de acordo com seu tamanho
                  for item in range(len(resultado)):
                    print(" {:<10} | {:<10} | {:<10} | {:<5} | {:<10} | {:<10}".format(
                      resultado[item][0], resultado[item][1],resultado[item][2],resultado[item][3],resultado[item][4],resultado[item][5]))
                  input(
                      f"{Cores.BOLD}{Cores.OKBLUE}\n\nPressione <ENTER> para continuar ...{Cores.ENDC}"
                  )
              else:
                  print(
                      f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
          except: 
                print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
        
def finalizar(pedidofechado,id):
      print(f'{Cores.BOLD}{Cores.Cyan}\nO VALOR TOTAL DO PEDIDO É DE R${pedidofechado}{Cores.ENDC}')
      input(
          f"{Cores.BOLD}{Cores.Red }\n\nPressione <ENTER> para PAGAR ...{Cores.ENDC}" 
       )
          
      print(f'{Cores.BOLD}{Cores.LightYellow}\n\nO VALOR DE R${pedidofechado} FOI PAGO COM SUCESSO.{Cores.ENDC} OBRIGADO!')
      sleep(2)


