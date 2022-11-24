"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Infos:
    - Generators podem ser criados com funções geradoras;
    - Funções geradores utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;
    
Diferenças entre Funções e Generator Functions 

---------------------------------------------------------------------------------
| Funções                               | Generator Functions                       
| utilizam return                       | utilizam yeld
| retorna uma vez                       | podem utilizar yield multiplas vezes
| quando executada, retorna um valor    | quando executada, retorna um generator
"""

# Exemplo Generator Function (gera um generator)    

def conta_ate(valor_maximo): # yield continua na função esperando o próximo next
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
        
gen = conta_ate(15)

for num in gen:
    print(num)