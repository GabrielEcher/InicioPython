"""
Preservando metadata com wraps

Metadatas(metadados) -> Dados intrisecos em arquivos, pixeis, data de mod, tamanho, etc

wraps -> Funções que envolvem elementos com diversas finalidades


# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        #Função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    ###Soma dois números.###
    return a + b

print(soma(3123, 31023))

print(soma.__name__) #Função (logar) dentro de outra
print(soma.__doc__)  Aqui a documentação:
"""

# Resolução do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao) # PRESERVA OS METADATAS DAS NOSSAS FUNÇÕES
    def logar(*args, **kwargs):
        #Função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b

print(soma(3123, 31023))

print(soma.__name__) # logar
print(soma.__doc__)  # ###Função (logar) dentro de outra###