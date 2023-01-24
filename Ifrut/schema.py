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

def criar_tabelas(banco):
	# Definindo a conexão com o BD chamado
 banco='IFRUT'
 c = Conexao()
 c.connect()  

 try: 
      # Criar tabela clientes----------------------------------------------------------
      c.execute("""CREATE TABLE if not exists clientes ( 
        idclient integer primary key,
        nome text,
        cpf text,
        endereco text,
        bairro text,
        cidade text,
        estado text,
        tel text,
        data data,
        usuario text,        
        senha integer)""")
      c.persist() 
      c.execute("""CREATE TABLE if not exists carrinho ( 
        idcarrinho integer,         
        idclient integer ,
        idproduto integer,
        qtde integer,
        descricao text,
        preco decimal(5,2),
        FOREIGN KEY (idclient)REFERENCES clientes (idclient) ,
        FOREIGN KEY (idproduto)REFERENCES produtos (idproduto)
        )""")
      c.persist() 
      #adicionar valores tabela clientes  ----------------------------------------------------------
      c.execute("INSERT INTO clientes  VALUES (1,'Julio', '12563289923','Rua das papoulas 35','Vila biachi','bragança paulista','SP','(11) 2577-9876', '22-11-2020','Julio', 123),(2,'luis', '12563289923','Rua das papoulas 35','Vila biachi','bragança paulista','SP','(11) 2577-9876', '22-11-2020','luis', 123);")
      c.persist() 
      c.execute("""CREATE TABLE if not exists produtos ( 
        idvendedor integer,           
        idproduto integer primary key,     
        descricao text,
        categoria integer,
        data data,
        preco decimal(5,2),
        FOREIGN KEY (idvendedor)REFERENCES vendedores (idvendedor))""")
      c.persist() 
      #adicionar valores tabela clientes  ----------------------------------------------------------
      c.execute("INSERT INTO produtos  VALUES (1,1,'batata',2,'22-11-2020',2.50),(1,2,'couve', 2,'22-11-2020',3.00),(2,3,'berinjela',2,'12-11-2020',1.25),(1,4,'Beterraba', 2,'22-11-2020',4.50),(2,5,'Couve-flor',2,'22-11-2020',2.00),(1,6,'Banana/Duzia',1,'22-11-2020',3.00), (1,7,'Mandioca',2,'25-11-2020',3.00),(2,8,'Quiabo',2,'27-11-2020',1.00),(2,9,'Maço de hortelâ',3,'28-11-2020',2.00),(1,10,'Pepino',2,'22-11-2020',2.50), (1,11,'laranja',1,'22-11-2020',1.00),(2,12,'Tomate',1,'23-11-2020',1.00);")
      c.persist() 
      c.execute("""CREATE TABLE if not exists vendedores ( 
        idvendedor integer primary key,
        nome text,
        nomeempresa text,
        cnpj text,
        endereco text,
        bairro text,
        cidade text,
        estado text,
        tel text,
        data data,
        usuario text,        
        senha integer)""")
      c.persist() 
      c.execute("INSERT INTO vendedores  VALUES (1,'Juliano','casa das ervas' ,'536346','Rua das rosas 35','Vila verde','bragança paulista','SP','(11) 2277-93876', '22-11-2020','Julio', 123);")
      c.persist() 

 
      c.execute("""CREATE TABLE if not exists vendas (
        idvenda integer primary key,
        idclient integer,
        idproduto integer,
        descricao text,
        qtde int,
        preco decimal(5,2),
        data date,
        idvendedor integer,    
        FOREIGN KEY (idvendedor)REFERENCES produtos (idvendedor)
        FOREIGN KEY (idclient)REFERENCES clientes (idclient)
        FOREIGN KEY (idproduto)REFERENCES produtos (idproduto)
        )""")
      c.persist() 
      c.execute("INSERT INTO vendas VALUES (1,2,3,'descricao',3,'23.50','22-11-2020',1);")
      c.persist() 
  
        
 except Error as e:
    None