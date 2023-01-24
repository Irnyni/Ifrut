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
import carrinho
import random

banco = 'IFRUT'
c = Conexao()
c.connect()
usuario = ''
id = 1


def criarvendedor():
    limpar()
    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
    print(
        f'{Cores.BOLD}{Cores.Yellow}\n\t\t\t\tCADASTRAR COMO vendedor\n\n{Cores.ENDC}'
    )
    nome = input("Nome do produtor: ").title()
    nomeempresa = input("Nome empresa: ").title()
    cnpj = input("CNPJ: ")
    endereco = input("Endereço: ").title()
    bairro = input("Bairro: ").title()
    cidade = input("Cidade: ").title()
    estado = input("Estado: ").title()
    tel = input("Telefone: ").title()
    data = format(date.today(), '%d-%m-%Y')
    usuario = input("Usuario: ").title()
    senha = int(input("senha: "))
    novovendedor = vendedor(nome, nomeempresa, cnpj, endereco, bairro, cidade,
                            estado, tel, data, usuario, senha)
    vendedor.inserir(novovendedor)


def criarpessoa():
    limpar()
    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
    print(
        f'{Cores.BOLD}{Cores.Yellow}\n\t\t\t\t\tCADASTRAR COMO CLIENTE\n\n{Cores.ENDC}'
    )
    nome = input("Nome do cliente: ").title()
    cpf = input("CPF: ")
    endereco = input("Endereço: ").title()
    bairro = input("Bairro: ").title()
    cidade = input("Cidade: ").title()
    estado = input("Estado: ").title()
    tel = input("Telefone: ").title()
    data = format(date.today(), '%d-%m-%Y')
    usuario = input("Usuario: ").title()
    senha = int(input("senha: "))
    novapessoa = pessoa(nome, cpf, endereco, bairro, cidade, estado, tel, data,
                        usuario, senha)
    pessoa.inserir(novapessoa)


def pesquisarpv(id):
    limpar()
    id = str(id)
    try:
        c = Conexao()
        c.connect()
        c.execute("SELECT * FROM produtos WHERE idvendedor like (?);",
                  ('%' + id + '%', ))
        resultado = c.fetchall()
        if resultado:
            #Mostrar itens do cliente-----------------------------------------------------
            print(f"{Cores.BOLD}{Cores.Red}")
            print("{:<6} | {:<6} | {:<15} | {:<6} | {:<10} | {:<10} ".format(
                "IDVend", "IDProd", "DESCRICAO", "CATEG", "DATA",
                "PREÇO"))  # titulo dos dados apresentados -------
            print(65 * '*' + f"{Cores.ENDC} ")

            #mostrar cada item de acordo com seu tamanho
            for item in range(len(resultado)):
                print(
                    "{:<6} | {:<6} | {:<15} | {:<6} | {:<10} | {:<10} ".format(
                        resultado[item][0], resultado[item][1],
                        resultado[item][2], resultado[item][3],
                        resultado[item][4], resultado[item][5]))
            input(
                f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}"
            )
        else:
            print(
                f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}"
            )
    except:
        print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
        input(
            f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}"
        )


def vendas(id):
    id = str(id)
    try:
        c = Conexao()
        c.connect()
        c.execute("SELECT * FROM vendas WHERE idvendedor like (?);",
                  ('%' + id + '%', ))
        resultado = c.fetchall()
        limpar()
        print(
            f'{Cores.BOLD}{Cores.Yellow}{Cores.UNDERLINE}\n\t\t\t\t\tRESUMO DAS VENDAS\n\n{Cores.ENDC}'
        )
        if resultado:
            #Mostrar itens do cliente-----------------------------------------------------
            print(f"{Cores.BOLD}{Cores.Red}")
            print("{:<8} | {:<8} | {:<10} | {:<15} | {:<10} | {:<10} | {:<10}".
                  format(
                      "IDVenda",
                      "IDProd",
                      "IDCLIENTE",
                      "DESCRICAO",
                      'QTDE',
                      "PREÇO",
                      "DATA",
                  ))  # titulo dos dados apresentados -------
            print(75 * '*' + f"{Cores.ENDC} ")

            #mostrar cada item de acordo com seu tamanho
            for item in range(len(resultado)):
                print(
                    "{:<8} | {:<8} | {:<10} | {:<15} | {:<10} | {:<10} | {:<10}"
                    .format(resultado[item][0], resultado[item][1],
                            resultado[item][2], resultado[item][3],
                            resultado[item][4], resultado[item][5],
                            resultado[item][6]))
            input(
                f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}"
            )
        else:
            print(
                f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}"
            )
    except:
        print(f"{Cores.BOLD}{Cores.FAIL}ERRO NA PESQUISA DE DADOS{Cores.ENDC}")
        input(
            f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para continuar ...{Cores.ENDC}"
        )


def usuarios(login):
    while login > 0 and login <= 3:

        if login == 1:

            login = verificacao(login)

        if login == 2:

            login = verificacao(login)

        if login == 3:
            for i in range(3):
                print(
                    f'{Cores.BOLD}{Cores.Yellow}\n\tENCERRANDO O BANCO!!!\n\n{Cores.ENDC}'
                )
                sleep(0.05)
                limpar()

            sleep(0.5)
            limpar()
            print(
                f'{Cores.BOLD}{Cores.LightGreen}\n\tFINALIZADO!!!\n\n{Cores.ENDC}'
            )
            break


#Menu de opções Principais----------------------------
def chamada(opcaovsub, opcaocsub, login):
    global id, usuario
    c = Conexao()
    c.connect()
    c.execute("SELECT idclient FROM clientes WHERE usuario like (?);",
              ('%' + usuario + '%', ))
    id = c.fetchall()
    if id:
        id = id[0][0]
    if opcaocsub == 1:
        compra = 1
        idcarrinho = random.randrange(1, 999999)
        while (compra != '0'):
            limpar()
            produto.pesquisar({})
            compra = input(
                f"{Cores.BOLD}{Cores.Cyan}\n\nDIGITE ID PRODUTO OU 0 PARA FINALIZAR O PEDIDO: {Cores.ENDC}"
            )
            if (compra != '0'):
                qtde = int(
                    input(
                        f"{Cores.BOLD}{Cores.Cyan}\n\nINSIRA A QUANTIDADE QUE DESEJA COMPRAR: {Cores.ENDC}"
                    ))

                try:
                    c = Conexao()
                    c.connect()
                    c.execute(
                        "SELECT idclient FROM clientes WHERE usuario like (?);",
                        ('%' + usuario + '%', ))
                    id = c.fetchall()
                    id = id[0][0]
                    c.execute(
                        "SELECT preco FROM produtos WHERE idproduto like (?);",
                        ('%' + compra + '%', ))
                    preco = c.fetchall()
                    preco = preco[0][0]
                    c.execute(
                        "SELECT descricao FROM produtos WHERE idproduto like (?);",
                        ('%' + compra + '%', ))
                    desc = c.fetchall()
                    desc = desc[0][0]
                    c.execute(
                        "SELECT idproduto FROM produtos WHERE idproduto like (?);",
                        ('%' + compra + '%', ))
                    idpro = c.fetchall()
                    if (idpro):
                        idpro = idpro[0][0]

                    c.execute(
                        "SELECT idvendedor FROM produtos WHERE idproduto like (?);",
                        ('%' + compra + '%', ))
                    idvend = c.fetchall()
                    idvend = idvend[0][0]
                    data = format(date.today(), '%d-%m-%Y')
                    acumulado = (idcarrinho, id, idpro, qtde, desc, preco)
                    venda = (idpro, id, qtde, desc, preco, data, idvend)
                    c.execute(
                        "INSERT INTO carrinho (idcarrinho,idclient,idproduto,qtde,descricao,preco) VALUES (?,?,?,?,?,?);",
                        acumulado)
                    c.persist()  # grava no BD
                    c.execute("SELECT * FROM carrinho ;")
                    c.execute(
                        "INSERT INTO vendas (idproduto,idclient,qtde,descricao,preco,data,idvendedor) VALUES (?,?,?,?,?,?,?);",
                        venda)
                    c.persist()  # grava no BD
                    c.execute("SELECT * FROM vendas ;")
                    result = c.fetchall()
                    var1 = str(idcarrinho)

                    c = Conexao()
                    c.connect()
                    c.execute(
                        "SELECT sum(qtde*preco) FROM carrinho where idcarrinho like (?);",
                        ('%' + var1 + '%', ))
                    resultado = c.fetchall()
                    resultado = resultado[0][0]
                    print(resultado)
                except Error as e:
                    print(e)
                else:
                    print(
                        f"{Cores.BOLD}{Cores.OKGREEN}\n\nProduto adicionado ao carrinho!.{Cores.ENDC}"
                    )
                    input(
                        f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}"
                    )
                finally:
                    c.disconnect()
        carrinho.finalizar(resultado, id)

    elif opcaocsub == 2:
        limpar()
        carrinho.pesquisar(id)
    elif opcaocsub == 3:
        pessoa.atualizar({})
    elif opcaovsub == 1:
        limpar()
        c = Conexao()
        c.connect()
        c.execute("SELECT idvendedor FROM vendedores WHERE usuario like (?);",
                  ('%' + usuario + '%', ))
        id = c.fetchall()
        if id:
            id = id[0][0]
        print(
            f'{Cores.BOLD}{Cores.Yellow}\n\tINSERIR NOVOS PRODUTOS\n\n{Cores.ENDC}'
        )
        descricao = input("Insira a descricao do produto: ").title()
        categoria = int(input("Idcategoria: "))
        data = format(date.today(), '%d-%m-%Y')
        preco = input("Insira o valor: R$")
        preco = float(preco)
        produtonovo = produto(id, descricao, categoria, data, preco)
        produto.inserir(produtonovo)
    elif opcaovsub == 2:
        c.execute("SELECT idvendedor FROM vendedores WHERE usuario like (?);",
                  ('%' + usuario + '%', ))
        id = c.fetchall()
        if id:
            id = id[0][0]
        pesquisarpv(id)
    elif opcaovsub == 3:
        pesquisarpv(id)
        produto.atualizar({})
    elif opcaovsub == 4:
        produto.campodebusca({})
    elif opcaovsub == 5:
        pesquisarpv(id)
        produto.excluir({})
    elif opcaovsub == 6:
        c.execute("SELECT idvendedor FROM vendedores WHERE usuario like (?);",
                  ('%' + usuario + '%', ))
        id = c.fetchall()
        if id:
            id = id[0][0]
        vendas(id)
    if opcaocsub == 4:
        print(f'{Cores.WARNING}        <--- RETORNANDO{Cores.ENDC}')
        sleep(0.1)
        limpar()
        usuarios(login)

    if opcaovsub == 7:
        print(f'{Cores.WARNING}        <--- RETORNANDO{Cores.ENDC}')
        sleep(0.1)
        limpar()
        usuarios(login)
    opcaovsub = 10
    opcaocsub = 10
    print(f'\n\n login atual {login}')
    sleep(1)
    if (login == 2):
        opcaovsub = opcaov()
    if (login == 1):
        opcaocsub = opcaoc()


def menu():
    login = 0

    while login < 1 or login > 3:
        print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
        print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")

        print(
            f"{Cores.BOLD}{Cores.Cyan}\t\t\t******* - IFRUT - ******* \n\t\t   DA TERRA PARA SUA GELADEIRA!!!\n{Cores.ENDC}"
        )
        print(52 * f'{Cores.White }¨{Cores.ENDC}')  #Template cabeçalho
        print(
            f"{Cores.BOLD}{Cores.Yellow}\t\t\t***--  MENU DE OPÇÕES --***\n{Cores.ENDC}"
        )
        print(52 * f'{Cores.White }¨{Cores.ENDC}')  #Template cabeçalho
        print("\n")
        print(
            f"{Cores.BOLD}{Cores.WARNING}\n\t\t\t  1.{Cores.White}ENTRAR COMO CLIENTE {Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\n\t\t\t  2.{Cores.White}ENTRAR COMO VENDEDOR{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\n\t\t\t  3.{Cores.AMARELO}ENCERRAR\n\n{Cores.ENDC}"
        )
        print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
        print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
        login = int(input("\n\n\nESCOLHA A OPÇÃO DE LOGIN-> "))

        if login < 1 or login > 3:
            print(
                f"\n{Cores.BOLD}{Cores.LightYellow}ENTRADA INCORRETA!!! INSIRA UM VALOR REFERENTE AO MENU!!!\n\n{Cores.ENDC}"
            )
            limpar()
    limpar()
    return login


def opcaov():

    opcaovsub = 0

    while opcaovsub < 1 or opcaovsub > 6:
        limpar()
        tabela = 'ÁREA DO VENDEDOR'
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(f"{Cores.BOLD}{Cores.Red}\t\t*** {tabela} ***{Cores.ENDC}")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print('\n')
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t1.{Cores.White}ADICIONAR PRODUTOS{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t2.{Cores.White}CONSULTAR PRODUTOS GERAL{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t3.{Cores.White}ATUALIZAR PRODUTOS{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t4.{Cores.White}BUSCAR PRODUTOS{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t5.{Cores.White}EXCLUIR PRODUTOS{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t6.{Cores.White}HISTÓRICO DE VENDAS{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t7.{Cores.White}SAIR\n\n{Cores.ENDC}"
        )
        print(f"{Cores.OKBLUE}" + 20 * '-' + 12 * '*' + 20 * '-' +
              f"{Cores.ENDC}")
        print(f"\t\t\t{Cores.OKBLUE}" + 26 * '-' + f"{Cores.ENDC}")
        opcaovsub = int(input("ESCOLHA A OPERAÇÃO: "))
        if opcaovsub < 1 or opcaovsub > 7:
            print(
                f"\n\t{Cores.BOLD}{Cores.LightYellow}ENTRADA INCORRETA!!! INSIRA UM VALOR REFERENTE AO MENU!!!\n\n{Cores.ENDC}"
            )
        opcaocsub = 10
        login = 2
        chamada(opcaovsub, opcaocsub, login)


def opcaoc():
    opcaocsub = 0
    while opcaocsub < 1 or opcaocsub > 6:
        limpar()
        tabela = 'ÁREA DO CLIENTE'
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(f"{Cores.BOLD}{Cores.Red}\t\t*** {tabela} ***{Cores.ENDC}")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print(8 * f"{Cores.LightGreen }IFRUT")
        print('\n')
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t1.{Cores.White}VER CATALOGO{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t2.{Cores.White}CARRINHO {Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t3.{Cores.White}GERENCIAR PERFIL{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t4.{Cores.White}SAIR\n\n{Cores.ENDC}"
        )
        print(f"{Cores.OKBLUE}" + 20 * '-' + 12 * '*' + 20 * '-' +
              f"{Cores.ENDC}")
        print(f"\t\t\t{Cores.OKBLUE}" + 26 * '-' + f"{Cores.ENDC}")
        opcaocsub = int(input("ESCOLHA A OPERAÇÃO: "))
        if opcaocsub < 1 or opcaocsub > 4:
            print(
                f"\n\t{Cores.BOLD}{Cores.LightYellow}ENTRADA INCORRETA!!! INSIRA UM VALOR REFERENTE AO MENU!!!\n\n{Cores.ENDC}"
            )
        login = 1
        opcaovsub = 10
        chamada(opcaovsub, opcaocsub, login)


def verificacao(login):
    A = 0
    global usuario, id
    while (A < 1 or A > 3):
        print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
        print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")

        print(
            f"{Cores.BOLD}{Cores.Red }\t\t\t\t\tÁREA DE LOGIN\n\n\n\n\n{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t\t\t1.{Cores.White}JA TENHO CONTA{Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t\t\t2.{Cores.White}CRIAR CONTA {Cores.ENDC}"
        )
        print(
            f"{Cores.BOLD}{Cores.WARNING}\t\t\t\t\t3.{Cores.White}SAIR\n\n{Cores.ENDC}"
        )
        print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
        print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
        A = int(input("\n\nESCOLHA PARA FAZER LOGIN:  "))
        if (A < 1 or A > 3):
            print(
                f"\n\n{Cores.BOLD}{Cores.LightRed }ENTRADA INCORRETA! SELECIONE UMA OPÇÃO REFERENTE AO MENU!!!{Cores.ENDC}"
            )

    if (A == 1):
        if (login == 1):
            limpar()
            print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
            print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
            usuario = input(
                f"{Cores.Cyan  }\nINSIRA O NOME DE USUARIO CONSUMIDOR: {Cores.ENDC}"
            )
            senha = int(
                input(f"{Cores.Cyan  }\n\n\nINSIRA A SENHA: {Cores.ENDC}"))
            resultado = "0"
            c = Conexao()
            c.connect()
            c.execute("SELECT senha FROM clientes WHERE usuario like (?);",
                      ('%' + usuario + '%', ))
            resultado = c.fetchall()
            if (resultado):
                resultado = resultado[0][0]
                if (senha == resultado and login == 1):
                    print("\n\n\t\t\t\t\t\t\tACESSANDO...")
                    sleep(1)
                    opcaocsub = opcaoc()
                    return opcaocsub
                else:
                    print(
                        f"\n {Cores.BOLD}{Cores.Red }\t\t\t\t\tUSUARIO OU SENHA INCORRETOS!!!{Cores.ENDC}"
                    )
                    sleep(1)
                    limpar()
            else:
                print(
                    f"\n{Cores.BOLD}{Cores.Red }\t\t\t\t\tUSUARIO OU SENHA INCORRETOS!!!{Cores.ENDC}"
                )
                sleep(1)
                limpar()
        if (login == 2):
            limpar()
            print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
            print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
            usuario = input(
                f"{Cores.Cyan  }\nINSIRA O NOME DE USUARIO VENDEDOR: {Cores.ENDC}"
            )
            senha = int(
                input(f"{Cores.Cyan  }\n\n\nINSIRA A SENHA: {Cores.ENDC}"))
            c = Conexao()
            c.connect()
            c.execute("SELECT senha FROM vendedores WHERE usuario like (?);",
                      ('%' + usuario + '%', ))
            resultado1 = c.fetchall()
            if (resultado1):
                resultado1 = resultado1[0][0]
                if (senha == resultado1 and login == 2):
                    print("\n\n\t\t\t\t\t\t\tACESSANDO...")
                    sleep(2)
                    opcaovsub = opcaov()
                    return opcaovsub

                else:
                    print(
                        f"\n {Cores.BOLD}{Cores.Red }\t\t\t\t\tUSUARIO OU SENHA INCORRETOS!!!{Cores.ENDC}"
                    )
                    sleep(1)
                    limpar()
            else:
                print(
                    f"\n{Cores.BOLD}{Cores.Red }\t\t\t\t\tUSUARIO OU SENHA INCORRETOS!!!{Cores.ENDC}"
                )
                sleep(1)
                limpar()
    if (A == 2):
        if (login == 1):
            criarpessoa()
        if (login == 2):
            criarvendedor()

    if (A == 3):
        print(f'\n{Cores.WARNING}        <--- RETORNANDO{Cores.ENDC}')
        sleep(1)
        limpar()
        login = menu()

    return login


# Função para limpar a tela antes de exibir a próxima instrução
def limpar():
    # Importando o módulo do sistema operacional (os) para usar instruções dele
    import os
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


if __name__ == '__main__':
    limpar()
    opcaocsub = 0
    opcaovsub = 0
    login = 0

    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow }IFRUT{Cores.ENDC}")
    print(
        f"{Cores.BOLD}{Cores.Red}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    )
    print(">@@>>>>>@@@@@@@@>>>@@@@@@>>>>>>>>@@>>>>>>>>@@>>>@@@@@@@@@@@>")
    print(">@@>>>>@@@>>>>>>>>>@@>>>@@@@>>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>>@@@>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>>@@@>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>@@@>>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@@@@@@@>>>>@@@@@@@>>>>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>@@@>>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>>@@>>>>>@@>>>>>>>>@@>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>>>@@>>>>>@@>>>>>>@@>>>>>>>>@@@>>>>>")
    print(">@@>>>>@@>>>>>>>>>>@@>>>>>>@@@>>>>>@@@@@@@@>>>>>>>>>@@@>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow  }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightGreen }IFRUT{Cores.ENDC}")
    print(12 * f"{Cores.LightYellow  }IFRUT{Cores.ENDC}")
    print('\n')
    sleep(2)
    input(
        f"{Cores.BOLD}{Cores.Cyan }\n\n\tPRESSIONE ENTER PARA UMA ALIMENTAÇÃO SAUDÁVEL ! ...{Cores.ENDC}"
    )

    # Executando a função de criação da conexão com o banco de dados
    banco = 'IFRUT'
    conecta = Conexao()
    conecta.connect()
    schema.criar_tabelas(banco)
    c = Conexao()
    c.connect()
    var = '1'
    sleep(1)
    #input(
    # f"{Cores.BOLD}{Cores.OKBLUE}\n\n\n\t\t\tPressione <ENTER> para continuar ...{Cores.ENDC}"
    # )
    limpar()
    login = menu()
    usuarios(login)
