import dadospessoa
import sqlite3
import os
from sqlite3 import Error

def Menu():
    try:
        os.system('cls')
        print("1 - Consultar pessoas cadastradas")
        print("2 - Incluir nova pessoa")
        print("3 - Atualizar cadastro")
        print("4 - Deletar cadastro")
        print("5 - Finalizar programa")
    except:
        print("ERRO: menu não pode ser aberto")

opc = 0
while opc != 5:
    
    Menu()
    opc = int(input("Digite a opção: "))

    if opc == 1:
        os.system('cls')
        print('Lista de perfis cadastrados - Dados Pessoais:')
        print('----------------------------------------')
        dadospessoa.viewData()
        print('----------------------------------------')
        os.system('pause')
    elif opc == 2:
        os.system('cls')
        dadospessoa.insertData()
    elif opc == 3:
        os.system('cls')
        dadospessoa.updateData()
    elif opc == 4:
        os.system('cls')
        dadospessoa.delData()

dadospessoa.con.close()
os.system('cls')
print('Obrigado por utilizar o Kriador de curriculoS')
print('By: Kaleu S. Rodrigues')