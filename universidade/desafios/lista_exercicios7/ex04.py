from random import  randint #importar funcao
'''
1-Simule o lancamento de um dado n vezes
2-calcule o percentual de surgimento de cada face do dado
3- Imprima o percentual para o usuario
4- Encerre o programa se o usuario pressionar 0
5- Use um array para armazenar o número de surgimentos de cada face
Não consegui seguir adiante
'''
#1
def simular_dado(): # funcao simular dado
    dado = list() #Criar lista vazia para as faces do dado
    cont = list()#Criar lista vazia para o contador das ocorrencias do dado
    n = int(input("Quantas vezes deseja lançar?: [0 para sair]"))
    i = 0 #iniciar indíce
    while n != 0 or n <= i : # encerrar programa
        dado[i] = randint(1,6) #o elemento localizado no indice i, armazena um inteiro aleatório no intevalo [1:6]
        if dado[i] in dado: # se elemento[i] está no array
            cont[i] += 1 # contador do elemento incrementa
        else:
            cont[i] = 1 # contador do elemento inicia
        i += 1
    return dado ,  cont
print(simular_dado())
'''
o percentual de surgimento de uma face de um dado pode ser dado pela funcao matematica
f(x) = x/y * 100 ; onde x é a quantidade de ocorrencias  e y o tamanho da lista
1- obter a quantidade de ocorrencia de x
 -usando um contador que incrementa 1 a cada aparicao de x
2- obter tamanho da lista -> é uma constante que pode ser obtida a partir da funcao len(nome_lista)
'''
def percentual_surgimento_x (x , y):
    percentual = x/y * 100
   

 
