a = int(input("Digite um valor menor que 10000: ")) #Valor a inteiro menor que 10000
b = int(input("Digite um valor menor que 10000: ")) #Valor b inteiro menor que 10000

str_a = str(a)
str_b = str(b)

list_a = []
list_b = []

for posicao in str_a:
    list_a.append(int(posicao))
    
list_a.reverse() # Descobrimos o algarismo menos significativo
    
for posicao in str_b:
    list_b.append(int(posicao))

list_b.reverse() # Descobrimos o algarismo menos significativo

list_a.reverse() # Revertido o que foi feito antes, para realizar a soma
list_b.reverse() # Revertido o que foi feito antes, para realizar a soma

str_a = "" 

for pos in list_a:
    str_a += str(pos)     # str += "5" + "4" +"3" ==> "543"
    
if len(str_a)>0:
    new_a = int(str_a)

print(new_a)

str_b = ""
for pos in list_b:
    str_b += str(pos)
    
if len(str_b)>0:
    new_b = int(str_b)

print(new_b)

soma = new_a + new_b
print(soma)