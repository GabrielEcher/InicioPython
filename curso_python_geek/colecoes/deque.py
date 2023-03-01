"""
Módulo Collections - Deque

Deque é uma lista de alta performance
"""

from collections import deque

#Criando deques

deq = deque('echer')

print(deq)

#Adicionando elementos no deque

deq.append('y')
print(deq)

deq.appendleft('o')
print(deq)

print(deq.pop())  #REMOVE E RETORNA O ULT ELEMENTO
print(deq)

print(deq.popleft())
print(deq)