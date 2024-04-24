"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""

velocidade = 62 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde está o radar 1
RADAR_RANGE = 1 # distancia que o radar pega


velocidade_passou_radar = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_passou_radar


if velocidade_passou_radar :
    print('Velocidade do carro passou do radar 1')

if carro_multado_radar_1:
        print('carro multado por execesso de velocidade')