import random

n = int(input('Digite o número de lançamentos do dado: '))
while n != 0:
  lista = [0]*6
  for i in range(n):
    face = random.randint(1,6)  ## valor aleatório entre 1 e 6
    lista[face-1] += 1
  for i in range(len(lista)):
    lista[i] = lista[i]/n
  print(lista)
  n = int(input('Digite o número de lançamentos do dado: '))
   

 
