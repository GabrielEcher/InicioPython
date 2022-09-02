"""
Programa que recebe a e b(positivos menores que 10000) e:
- Criar um vetor onde cada posição é um algarismo do número. A primeira
posição é o algarismo menos significativo


"""
a = int(input('Digite o primeiro valor entre 0 e 9999: '))
b = int(input('Digite o segundo valor entre 0 e 9999: '))
lista_c = []
acim_10 = [0, 0, 0, 0, 0]
 
lista_a = list(str(a))
lista_b = list(str(b))
lista_a.reverse()
lista_b.reverse()

lista_a = list(lista_a)
lista_b = list(lista_b)
print(lista_a, lista_b)