"""
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condições no mesmo if (ruim)

    <- Contagem de complexidade (ruim)

"""

velocidade = 61  # velocidade atual do carro
local_carro = 98 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1


if velocidade_carro_passou_radar1:
    print('Velocidade carro passou do radar 1')
    
if carro_passou_radar1:
    print('Carro passou radar 1')
    
if carro_multado_radar1:
    print('Carro multado em radar 1')