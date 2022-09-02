"""
Função que recebe 3 inteiros como parametro, representando horas, minutos e segundos
e os converta em segundos
"""

horas = int(input("Digite a hora: "))
mins = int(input("Digite os minutos: "))
seg = int(input("Digite os segundos: "))

def converter_p_segundos(horas, mins, seg):
    horas_c = horas * 3600
    mins_c = mins * 60
    total_convertido = horas_c + mins_c + seg
    return f'O total em segundos passados é: {total_convertido}'

print(converter_p_segundos(horas, mins, seg))