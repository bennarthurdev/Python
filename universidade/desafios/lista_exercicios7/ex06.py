from math import sqrt

#distancias
def distancia_entre_pontos():
    distancia = sqrt(2)
    return distancia
'''
não consegui desenvolver essa etapa
OUT:
um array de distancias entre os pontos
'''
def distancia_maxima(distancia):
    if distancia[i]>distancia[i-1]:
        distancia_maxima = distancia[i]
    return distancia_maxima
def distancia_minima(distancia):
    if distancia[i]<distancia[i-1]:
        distancia_minima = distancia[i]
        return distancia_minima
    
def distancia_media(soma_distancia, distancia):
    media = soma_distancia/len(distancia)
    return media
#ler n cordenadas
'''
1 - criar uma lista de n tuplas
2 - cada tupla deve conter as coordenadas de um ponto 
'''
n = int(input("Quantas coordenadas você deseja calcular?"))
coordenadas = [None]*n
for i  in range(len(coordenadas)):
     x , y = int(input("X:")) , int(input("Y:"))
     coordenadas[i] = (x,y)
print(coordenadas)
