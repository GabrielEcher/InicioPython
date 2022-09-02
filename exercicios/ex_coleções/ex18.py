import random
 
lista = [2, 4, 6, 12, 24, 48, 64, 80, 9, 81]
multiplos = []
indice = random.randint(0, len(lista) - 1)

print(f"Número x escolhido:{lista[indice]}")

for numero in lista:
    if numero % lista[indice] == 0 and numero - lista[indice] != 0:
        multiplos.append(numero)

print(f"Os multiplos do numero {lista[indice]}, são: {str(multiplos).strip('[]')}")
print("\nCaso não seja mostrado nenhum número é porque esse número não possui múltiplos, ou possui apenas o próprio "
      "número como múltiplo")
