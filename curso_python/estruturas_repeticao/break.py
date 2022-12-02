"""
Serve para sair dos loops




for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Saí do loop")
"""

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break