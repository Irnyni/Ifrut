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
class vendedor:

    def __init__(self,nome,nomeempresa,cnpj,endereco,bairro,cidade,estado,tel,data,usuario,senha):
        c = Conexao()
        c.connect()  
        self.nome = nome
        self.nomeempresa=nomeempresa
        self.cnpj = cnpj
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self. tel= tel
        self.data = data
        self.usuario = usuario
        self.senha= senha
    def inserir(self):
        try:
            c = Conexao()
            c.connect()  
            c.execute
            os.system("clear")  #limpa a tela 
            vendedornovo =(self.nome,self.nomeempresa,self.cnpj,self.endereco,self.bairro,self.cidade,self.estado,self.tel,self.data,self.usuario,self.senha)
            c.execute("INSERT INTO vendedores(nome,nomeempresa,cnpj,endereco,bairro,cidade,estado,tel,data,usuario,senha) VALUES (?,?,?,?,?,?,?,?,?,?,?);",vendedornovo)
            c.persist()  # grava no BD
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}Perfil criado com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
            limpar()
        finally:
            c.disconnect()
           
      
    def pesquisar(self):
        try:
            c = Conexao()
            c.connect()  
            c.execute("SELECT * FROM vendedores;")
            resultado = c.fetchall()  
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tMOSTRAR DADOS DOS CLIENTES\n\n{Cores.ENDC}')                      

            if resultado: 
    #Mostrar itens do cliente-----------------------------------------------------
                print(f"{Cores.BOLD}{Cores.Red}")
                print(" {:<2} | {:<15} | {:<15} | {:<12} | {:<20} | {:<12} | {:<20} | {:<3} | {:<15} | {:<12} ".format(
                    "ID","NOME","NOMELOJA","CNPJ","ENDEREÇO","BAIRRO","CIDADE","UF","TEL","INSERÇÃO")) # titulo dos dados apresentados -------
                print(130 * '*' + f"{Cores.ENDC} ")

    #mostrar cada item de acordo com seu tamanho
                for item in range(len(resultado)):
                    print(" {:<2} | {:<15} | {:<15} | {:<12} | {:<20} | {:<12} | {:<20} | {:<3} | {:<15} | {:<12} ".format(
                    resultado[item][0], resultado[item][1],resultado[item][2], resultado[item][3],resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7], resultado[item][8], resultado[item][9]))
                input(
                    f"{Cores.BOLD}{Cores.OKBLUE}\n\nPressione <ENTER> para continuar ...{Cores.ENDC}"
                )
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
            limpar()
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tATUALIZAR DADOS \n{Cores.ENDC}')                
  #Menuzinho com opções do que atualizar -----------------------------
            #Opções de atualizar           
            print(f"{Cores.WARNING}1.{Cores.ENDC} Nome{Cores.ENDC}")
            print(f"{Cores.WARNING}2.{Cores.ENDC} CPF{Cores.ENDC}")
            print(f"{Cores.WARNING}3.{Cores.ENDC} Endereço{Cores.ENDC}")
            print(f"{Cores.WARNING}4.{Cores.ENDC}{Cores.ENDC} telefone{Cores.ENDC}")
            print(f"{Cores.WARNING}5.{Cores.ENDC} Sair{Cores.ENDC}")   
            opcaoatt = input("Indique a informação que deseja atualizar: \n")           
        #opção att 1 --------------------------------------
            if opcaoatt=='1':
                x = input("Insira o id do nome a ser atualizado:")     
                novonome = input("Insira o novo nome:").title()
                att=(novonome,x)              
                c.execute("UPDATE clientes SET nome=? where idclient=?;",att)
                c.persist()  # grava no BD
                
                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!.{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

        #opção att 2 --------------------------------------
            if opcaoatt=='2':
                x = input("Insira o id do CPF a ser atualizado:").upper()       
                novocpf = input("Insira o novo CPF:").upper()
                att=(novocpf,x)              
                c.execute("UPDATE clientes SET cpf=? where idclient=?;",att)
                c.persist()  
                
                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

        #opção att 3 --------------------------------------
            if opcaoatt=='3':
                x = input("Insira o id do endereço a ser atualizado: ").upper()       
                novoendereco = input("Insira o novo endereço:").upper()
                novobairro = input("Insira o bairro:").upper()
                novacidade = input("Insira a cidade:").upper()
                novoestado = input("Insira o estado:").upper()
                att=(novoendereco,x) 
                attb=(novobairro,x)  
                attc=(novacidade,x)  
                atte=(novoestado,x)  
                c.execute("UPDATE clientes SET endereco=? where idclient=?;",att)
                c.execute("UPDATE clientes SET bairro=? where idclient=?;",attb)
                c.execute("UPDATE clientes SET cidade=? where idclient=?;",attc)
                c.execute("UPDATE clientes SET estado=? where idclient=?;",atte)
                c.persist()  # grava no BD

                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

              
        #opção att 4 --------------------------------------
            if opcaoatt=='4':
                x = input("Insira o id do telefone a ser atualizado:").upper()       
                novotel = input("Insira o novo telefone: ").upper()
                att=(novotel,x)              
                c.execute("UPDATE clientes SET tel=? where idclient=?;",att)
                c.persist()  # grava no BD

                #Aviso sucesso
                print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização feita com sucesso!.{Cores.ENDC}")
                input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

          #opção att 5 --------------------------------------       
            if opcaoatt=='5':
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
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tPESQUISAR DADOS COM FILTROS EM CLIENTES\n\n{Cores.ENDC}')             
            print(f"{Cores.WARNING}1.{Cores.ENDC} Nome{Cores.ENDC}")
            print(f"{Cores.WARNING}2.{Cores.ENDC} CPF{Cores.ENDC}")
            print(f"{Cores.WARNING}3.{Cores.ENDC} Endereço{Cores.ENDC}")
            print(f"{Cores.WARNING}4.{Cores.ENDC}{Cores.ENDC} Telefone{Cores.ENDC}")
            print(f"{Cores.WARNING}5.{Cores.ENDC} Sair{Cores.ENDC}")   
            opcaoatt = input("ATRAVÉS DE QUAL INFORMAÇÃO FARÁ A BUSCA? ")  

            #SEPARAÇÃO VISUAL ----------------------
            print("\n")
            print(f"\t\t\t{Cores.OKBLUE}" + 26 * '-' + f"{Cores.ENDC}")  

    #opção att 1 --------------------------------------
            if opcaoatt=='1':    
                descricao = input("\n\nINSIRA PARA PESQUISAR POR NOME: ").title()
                c.execute("SELECT * FROM clientes WHERE nome like (?);",
                      ('%' + descricao + '%', ))
                c.persist()

    #opção att 2 --------------------------------------
            if opcaoatt=='2':
                descricao = input("INSIRA PARA PESQUISAR POR CPF: ").title()
                c.execute("SELECT * FROM clientes WHERE cpf like (?);",
                      ('%' + descricao + '%', ))
                c.persist()

    #opção att 3 --------------------------------------
            if opcaoatt=='3':
                descricao = input("INSIRA PARA PESQUISAR POR ENDEREÇO: ").title()
                c.execute("SELECT * FROM clientes WHERE endereco like (?);",
                      ('%' + descricao + '%', ))
                c.persist()

    #opção att 4 --------------------------------------
            if opcaoatt=='4':
                descricao = input("INSIRA PARA PESQUISAR POR TELEFONE: ").title()
                c.execute("SELECT * FROM clientes WHERE tel like (?);",
                      ('%' + descricao + '%', ))
                c.persist()   
            resultado = c.fetchall()
            limpar()
            print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tPESQUISAR DADOS COM FILTROS EM CLIENTES\n\n{Cores.ENDC}')            
            print(c.fetchall())           
            if resultado: 
    #Mostrar itens do cliente-----------------------------------------------------
                print(f"{Cores.BOLD}{Cores.Red}")
                print(" {:<2} | {:<10} | {:<10} | {:<22} | {:<15} | {:<19} | {:<5} | {:<12} | {:<12} ".format(
                    "ID","NOME","CPF","ENDEREÇO","BAIRRO","CIDADE","UF","TEL","INSERÇÃO")) # titulo dos dados apresentados -------
                print(130 * '*' + f"{Cores.ENDC} ")

    #mostrar cada item de acordo com seu tamanho
                for item in range(len(resultado)):
                  print(" {:<2} | {:<10} | {:<10} | {:<22} | {:<15} | {:<19} | {:<5} | {:<12} | {:<10} ".format(
                    resultado[item][0], resultado[item][1],resultado[item][2], resultado[item][3],resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7], resultado[item][8]))
                input(
                    f"{Cores.BOLD}{Cores.OKBLUE}\n\nPressione <ENTER> para continuar ...{Cores.ENDC}"
                )
            else:
                print(
                    f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
        except: 
              print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
              input( f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")


    def excluir(self,usuario):
      try:
   
        c = Conexao()
        c.connect()  
        c.execute("SELECT senha FROM senhas WHERE usuario like (?);",
                      ('%' + usuario + '%', ))
        resultado = c.fetchall()
        resultado=resultado[0][0]
        os.system("clear")  #limpa a tela
        print(f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\tEXCLUSAO DE DADOS\n\n{Cores.ENDC}')  
        x = int(input("Indique o id a excluir: "))
        values = (x, )
        c.execute("DELETE FROM clientes WHERE idclient = ?;", values)
        c.persist()  # grava no BD
    #aviso sucesso -----------
        print(
            f"{Cores.BOLD}{Cores.OKGREEN}Exclusão realizado com sucesso!{Cores.ENDC}"
        )  
    #aviso de erro -----------
      except:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Erro na operação de exclusao!{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}")

    def senhas(self):
          c = Conexao()
          c.connect()  
          c.execute("SELECT * FROM senhas;")
          resultado = c.fetchall()  
          print(resultado)
      
