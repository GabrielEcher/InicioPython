"""
Debugando com PDB
PDB -> Python Debugger

# Forma mais profissional para se fazer o debug, utilizando o debugger

# Para debugarmos precisamos importar a bibilioteca pdb e usar a função set_trace()

# Forma MANUAL

# COMANDOS

# l (listar onde estamos no código)

# n (próxima linha)

# p (imprime variavel)

# c (continua a execução - finaliza o debugging)

# No python atual o comando de debug se tornou uma função built_in chamada breakpoint
breakpoint()
nome = 'Gabriel'
sobrenome = 'Echer'
nome_completo = nome + ' ' + sobrenome
curso = 'python'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# OBS: Cuidado com conflitos entre nomes e variáveis e os comandos do pdb