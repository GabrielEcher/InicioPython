print("Criação de usuário e senha!")
user = input("Informe o usuário:  ")
senha = input("Informe a senha:  ")

while senha == user:
    print("ERRO: Senha não pode ser igual ao usuário!!!")
    user = input("Informe o usuário:  ")
    senha = input("Informe a senha:  ")

print(f"USUÁRIO: {user}")
print(f"SENHA: {senha}")
