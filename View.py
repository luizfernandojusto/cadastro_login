import os

from Model import *
from Controller import *


print("----> CADASTRO E LOGIN <----\n")

while True:
    op = int(input("OPÇÃO : [ 1 ] - Cadastro | [ 2 ] - Login | [ 0 ] - SAIR\n"))
    if op == 0:
        os.system("cls" if os.name == "nt" else "clear")
        break

    elif op == 1:
        print("-----> Realizar Cadastro\n")

        nome = input("Nome: ")
        email = input("E-mail: ")
        senha = input("Senha: ")

        os.system("cls" if os.name == "nt" else "clear")

        CadastroController().cadastrar(Cadastro(nome=nome, email=email, senha=senha))

    elif op == 2:
        print("-----> Login\n")

        email = input("Digite E-mail: ")
        senha = input("Digite a Senha: ")

        os.system("cls" if os.name == "nt" else "clear")

        LoginController().acesso(Cadastro(email=email, senha=senha))
