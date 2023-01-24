from time import sleep  # Importando o módulo do sqlite3 para manipularmos o banco de dados SQLITE3
from sqlite3 import Error
from datetime import date
from cores import Cores
import os
from limpar import limpar
from sqlite3 import Error
import sqlite3
from conexao import Conexao
banco='IFRUT'



class produto:
    
    def __init__(self,id,descricao,categoria,data,preco):
        self.descricao = descricao
        self.categoria= categoria
        self.data = data
        self.id=id
        self.preco = preco
        
    def inserir(self):
        try:
        
            c = Conexao()
            c.connect()  
            os.system("clear")  #limpa a tela
            produtonovo=(self.id,self.descricao, self.categoria,self.data,self.preco)
            c.execute("INSERT INTO produtos(idvendedor,descricao,categoria,data,preco) VALUES (?,?,?,?,?);",produtonovo)
            c.persist()  # grava no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso!!! {Cores.ENDC}") 
        except:
            print(f"{Cores.BOLD}{Cores.OKGREEN}Erro na operação de inserção!{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")


    def pesquisar(self):
        try:
            c = Conexao()
            c.connect()  
            c.execute("SELECT * FROM produtos")
            resultado = c.fetchall()  
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\t\t\t\t\tLISTA DE PRODUTOS\n\n{Cores.ENDC}')                      

            if resultado: 
    #Mostrar itens do cliente-----------------------------------------------------
                print(f"{Cores.BOLD}{Cores.Red}")
                print("{:<6} | {:<6} | {:<15} | {:<6} | {:<10} | {:<10} ".format(
                   "IDVend","IDProd","DESCRICAO","CATEG", "DATA","PREÇO")) # titulo dos dados apresentados -------
                print( 65 * '*' + f"{Cores.ENDC} ")

    #mostrar cada item de acordo com seu tamanho
                for item in range(len(resultado)):
                  print("{:<6} | {:<6} | {:<15} | {:<6} | {:<10} | {:<10} ".format(
                    resultado[item][0], resultado[item][1],resultado[item][2],resultado[item][3],resultado[item][4],resultado[item][5]))
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")
            else:
                print(
                    f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
        except: 
              print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
              input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")
  
    def atualizar(self):
        try:
            c = Conexao()
            c.connect()  
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tMANTER ESTOQUE\n{Cores.ENDC}')                
  #Menuzinho com opções do que atualizar -----------------------------
            #Opções de atualizar 

            print(f"{Cores.WARNING}1.{Cores.ENDC} DESCRIÇÃO{Cores.ENDC}")
            print(f"{Cores.WARNING}2.{Cores.ENDC} CATERGORIA{Cores.ENDC}")
            print(f"{Cores.WARNING}3.{Cores.ENDC} PREÇO{Cores.ENDC}")
            print(f"{Cores.WARNING}4.{Cores.ENDC} SAIR{Cores.ENDC}")   
            opcaoatt = input("Indique a informação que deseja atualizar: \n")           
        #opção att 1 --------------------------------------
            if opcaoatt=='1':
                x = input("Insira o id do PRODUTO a ser atualizado:")     
                novonome = input("Insira a descricao do produto: ").title()
                att=(novonome,x)              
                c.execute("UPDATE produtos SET descricao=? where idproduto=?;",att)
                c.persist()  # grava no BD
                
                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!.{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

        #opção att 2 --------------------------------------
            if opcaoatt=='2':
                x = input("Insira o id do PRODUTO a ser atualizado:")      
                categoria = input("Insira a nova categoria: ").upper()
                att=(categoria,x)              
                c.execute("UPDATE produtos SET categoria=? where idproduto=?;",att)
                c.persist()  
                
                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")
        #opção att 3 --------------------------------------
            if opcaoatt=='3':
                x = input("Insira o id do PRODUTO a ser atualizado:")      
                categoria = input("Insira o novo preço: R$  ").upper()
                att=(categoria,x)              
                c.execute("UPDATE produtos SET preco=? where idproduto=?;",att)
                c.persist()  
                
                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")
        
            if opcaoatt=='4':
                            print (f'{Cores.WARNING}        <--- RETORNANDO{Cores.ENDC}')
                            pass 
        except: #aviso de erro
          print(f"{Cores.BOLD}{Cores.FAIL}\nERRO NA INSERÇÃO DE DADOS!!!{Cores.ENDC}")
            
          input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")



  
    def campodebusca(self):
        try:
            c = Conexao()
            c.connect()  
            os.system("clear")  #limpa a tela
    
            #CABEÇALHO - SEPARAÇÃO 
            #opçõe do menuzinho
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tPESQUISAR DADOS COM FILTROS EM PRODUTOS\n\n{Cores.ENDC}')             
            print(f"{Cores.WARNING}1.{Cores.ENDC} DESCRIÇÃO{Cores.ENDC}")
            print(f"{Cores.WARNING}2.{Cores.ENDC} CATERGORIA{Cores.ENDC}")
            print(f"{Cores.WARNING}3.{Cores.ENDC} Sair{Cores.ENDC}")         
            opcaoatt = input("ATRAVÉS DE QUAL INFORMAÇÃO FARÁ A BUSCA? ")  

            #SEPARAÇÃO VISUAL ----------------------
            print("\n")
            print(f"\t\t\t{Cores.OKBLUE}" + 26 * '-' + f"{Cores.ENDC}")  

    #opção att 1 --------------------------------------
            if opcaoatt=='1':    
                descricaos = input("\n\nINSIRA PARA PESQUISAR POR DESCRICAO: ")
                c.execute("SELECT * FROM produtos WHERE descricao like (?);",
                      ('%' + descricaos + '%', ))
                c.persist()

    #opção att 2 --------------------------------------
            if opcaoatt=='2':
                descricao = input("INSIRA PARA PESQUISAR POR CATEGORIA: ").title()
                c.execute("SELECT * FROM produtos WHERE categoria like (?);",
                      ('%' + descricao + '%', ))
                c.persist()

    #opção att 3 --------------------------------------
            if opcaoatt=='12':

                c.execute("SELECT * FROM clientes WHERE endereco like (?);",
                      ('%' + descricao + '%', ))
                c.persist()

    #opção att 4 --------------------------------------
            if opcaoatt=='11':
                descricao = input("INSIRA PARA PESQUISAR POR TELEFONE: ").title()
                c.execute("SELECT * FROM clientes WHERE tel like (?);",
                      ('%' + descricao + '%', ))
                c.persist()   
            resultado = c.fetchall()  
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tLISTA DE PRODUTOS\n\n{Cores.ENDC}')                      

            if resultado: 
    #Mostrar itens do cliente-----------------------------------------------------
                print(f"{Cores.BOLD}{Cores.Red}")
                print(" {:<2} | {:<10} | {:<10} | {:<10} ".format(
                    "ID","DESCRICAO","CATEGORIA", "DATA")) # titulo dos dados apresentados -------
                print( 30 * '*' + f"{Cores.ENDC} ")

    #mostrar cada item de acordo com seu tamanho
                for item in range(len(resultado)):
                  print(" {:<2} | {:<10} | {:<10} | {:<10} ".format(
                    resultado[item][0], resultado[item][1],resultado[item][2],resultado[item][3]))
                input(
                    f"{Cores.BOLD}{Cores.OKBLUE}\n\nPressione <ENTER> para continuar ...{Cores.ENDC}"
                )
            else:
                print(
                    f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
        except: 
              print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
              input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

    def excluir(self):
      try:
        c = Conexao()
        c.connect()  
        x = int(input("\n\nIndique o id a excluir: "))
        values = (x, )
        c.execute("DELETE FROM produtos WHERE idproduto = ?;", values)
        c.persist()  # grava no BD
    #aviso sucesso -----------
        print(
            f"{Cores.BOLD}{Cores.OKGREEN}Exclusão realizado com sucesso!{Cores.ENDC}"
        )  
    #aviso de erro -----------
      except:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Erro na operação de exclusao!{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")