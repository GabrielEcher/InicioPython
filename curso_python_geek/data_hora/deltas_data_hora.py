"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyy 12:55:34.99923249
data_final = dd/mm/yyy 13:34:43.902103912

delta = data_final - data_inicial


data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2023, 2, 28, 0)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas')
"""

import datetime

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_compra + regra_boleto

print(vencimento_boleto)