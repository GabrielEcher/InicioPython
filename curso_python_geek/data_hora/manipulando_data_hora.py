"""
Manipulando data e hora

Python tem um módulo builtin para se trabalhar com data e hora chamado datetime

#print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now()) # 2023-02-23 08:13:17.585279 BR 23/02/2023

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))


# replace() para fazer ajustes na data e hora

inicio = datetime.datetime.now()

print(inicio)


inicio = inicio.replace(year=2050, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# RECEBENDO DADOS DO USUÁRIO E CONVERTENDO PARA DATA

evento = datetime.datetime(2019, 1, 2, 0)

print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyy): ")

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
"""

import datetime 

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))