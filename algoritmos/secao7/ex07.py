#variaveis
contador_total = 0
contador_sit_1 = 0
contador_sit_2 = 0
contador_sit_3 = 0
contador_sit_4 = 0

#entradas
identificador = int(input("Informe a identificação: "))

#processamento
while identificador != 0:
    print("1 - Necessidade de esfera.")
    print("2 - Necessidade de limpeza.")
    print("3 - Necessidade da troca do cabo ou conector.")
    print("4 - Quebrado ou inutilizável.")
    #entrada
    defeito = int(input("Informe o tipo de defeito: "))
    #processamento
    if defeito == 1:
        contador_sit_1 = contador_sit_1 + 1
    elif defeito == 2:
        contador_sit_2 = contador_sit_2 + 1
    elif defeito == 3:
        contador_sit_3 = contador_sit_3 + 1
    elif defeito == 4:
        contador_sit_4 = contador_sit_4 + 1
    contador_total = contador_total + 1
    identificador = int(input("Informe a identificação: "))
#entradas
p1 = float(contador_sit_1 / contador_total * 100.0)
p2 = float(contador_sit_2 / contador_total * 100.0)
p3 = float(contador_sit_3 / contador_total * 100.0)
p4 = float(contador_sit_4 / contador_total * 100.0)

print(f"Quantidade de mouses: {contador_total}")
print(      f"Situação                                         Quantidade                    Percentual")
print(f"1 - Necessidade de esfera                            {contador_sit_1}                            {p1:.2f}%")
print(f"2 - Necessidade de limpeza                           {contador_sit_2}                            {p2:.2f}%")
print(f"3 - Necessidade da troca do cabo ou conector.        {contador_sit_3}                            {p3:.2f}%")
print(f"4 - Quebrado ou inutilizável.                        {contador_sit_4}                            {p4:.2f}%")