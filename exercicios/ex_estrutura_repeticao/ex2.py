"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
import getpass

print("CADASTRO DE USUÁRIO")

usuario = str(input("Informe o usuário: "))
senha = getpass.getpass("Informe a sua senha: ")


while usuario == senha:
    print("ERRO 42091, SENHA E USUÁRIO NÃO PODEM SER IGUAIS")
    usuario = str(input("Informe o usuário: "))
    senha = getpass.getpass("Informe a sua senha: ")

else:
    print("USUÁRIO CADASTRADO COM SUCESSO")