import os
import sqlite3
from sqlite3 import Error

############## Conxão com Banco de Dados ##############
dbfile = 'C:\\Users\\magal\\Desktop\\input\\mysite\\db.sqlite3'
con = sqlite3.connect(dbfile)
cur = con.cursor()

############## Variavel global ##############
idPessoal = ""

############## Criar tabela para dados Pessoais - PESSOAL ##############
def createTable():
    try:
        cur.execute('''CREATE TABLE PESSOAL (
                        ID_PESSOAL INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME       VARCHAR (10, 200),
                        TELEFONE   VARCHAR (10, 11),
                        EMAIL      VARCHAR (10, 200),
                        NASCIMENTO VARCHAR (10, 100)
                    )''')
        con.commit()
    except Error as er:
        print(er)

############## Inserir Dados Pessoais na Tabela ##############
def insertData():
    flag = "n"
    while flag!="s":
        try:
            nome = input("Digite seu nome: ")
            telefone = input("Digite seu telefone: ")
            email = input("Digite seu email: ")
            nasc = input("Digite sua data de nascimento: ")
            dadosPessoais = "INSERT INTO PESSOAL (NAME, TELEFONE, EMAIL, NASCIMENTO) VALUES('"+nome+"', '"+telefone+"', '"+email+"', '"+nasc+"')"
            os.system('cls')
            print("Cadastro efetuado com sucesso!")
            flag = input("Deseja parar de cadastrar dados? [s/n]")
            cur.execute(dadosPessoais)
            os.system('cls')
            con.commit()
        except Error as er:
            print(er)

############## Consultar perfis de Dados Pessoais na Tabela ##############
def viewData():
    try:
        allData = "SELECT * FROM PESSOAL"
        registros = cur.execute(allData)
        for r in registros:
            print(r)
        con.commit()
    except Error as er:
        print(er)

############## Atualizar Dados Pessoais na Tabela ##############
def updateData():
    try:
        idPessoal = input("Escolha qual perfil deseja editar: ")
        newName = input("Digite o novo nome: ")
        newTel = input("Digite o novo telefone: ")
        newMail = input("Digite o novo email: ")
        newBorn = input("Digite a nova dota de nascimento: ")

        att = "UPDATE PESSOAL SET NAME = '"+newName+"', TELEFONE = '"+newTel+"', EMAIL = '"+newMail+"', NASCIMENTO = '"+newBorn+"' WHERE ID_PESSOAL = "+idPessoal+""
        cur.execute(att)
        con.commit()
    except Error as er:
        print(er)

############## Deletar Dados Pessoais na Tabela ##############
def delData():
    try:
        idPessoal = input("Escolha qual perfil deseja excluir: ")
        deletarPessoal = "DELETE FROM PESSOAL WHERE ID_PESSOAL="+idPessoal+""
        deletado = "SELECT * FROM PESSOAL WHERE ID_PESSOAL="+idPessoal+""
        deleted = cur.execute(deletado)
        for d in deleted:
            print(" O perfil: " + str(d) + " foi deletado com sucesso!")
        cur.execute(deletarPessoal)
        con.commit()
        os.system('pause')
    except Error as er:
        print(er)

############## Executar funções para teste ##############
createTable()
#insertData()
#updateData()
#viewData()
#con.commit()
#con.close()
