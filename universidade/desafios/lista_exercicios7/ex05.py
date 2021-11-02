''' FUNCOES NECESSARIAS '''
#funcao de maximo

def sexo_de_maximo(lista1 , lista2):  
    maximo = lista2[0]# valor de partida
    #maior elemento de lista1
    for x in range(len(lista1)-1): # 1 , 2 ,3 ... , 10
        if lista1[x] > lista1[x-1]:  #l[1] > l[0]; l[2] > l[1] ; ... l[10]>l[9] 
            maximo = lista2[x] # maximo recebe o maior valor na interacao
    return maximo
    '''
    Out: sexo do maior individuo
    '''

    '''
    Parametros: lista1 -> a lista que contém a altura dos indivíduos
                             lista2 -> lista que contém o sexo dos indivíduos
    '''
    
#funcao de minimo
def sexo_de_minimo(lista1 , lista2):
    minimo = lista2[0]# valor de partida
    #maior elemento de lista1
    for x in range(len(lista1)-1): # 1 , 2 ,3 ... , 10
        if lista1[x] < lista1[x-1]:  #l[1] < l[0]; l[2] < l[1] ; ... l[10]<[9] 
            minimo = lista2[x] # minimo recebe o menor valor na interacao
    return minimo
    '''
    Out: sexo do menor individuo
    '''
    '''
    Parametros: lista1 -> a lista que contém a altura dos indivíduos
                             lista2 -> lista que contém o sexo dos indivíduos
    '''
#funcao de soma
def soma(lista1):
    soma = 0
    for x in range(len(lista1)-1): # 0,1,2...9
        soma += lista1[x]#soma = soma + lista[x]
        print(soma)
    return soma
    '''
    Out: Soma dos elementos contidos na lista 1
    '''
    '''
    Parametros: lista1 -> a lista que contém a altura dos indivíduos
    '''
    
#funcao de media
def media(lista1):
    soma_lista1 = soma(lista1)
    tamanho_lista1 = len(lista1)
    print(soma_lista1 , tamanho_lista1)
    media_lista1 = soma_lista1/tamanho_lista1 #chama soma(), chama len() e calcula a media
    return media_lista1
    '''
    Out: media de uma determinada lista
    '''
    '''
    Parametros: lista1 -> a lista que contém a altura dos indivíduos de um determinado sexo
    '''

##criacao das lista nescessarias (ENTRADAS)
L_altura = list()
L_sexo = list()
lista_m = list()
lista_f = list()

for x in range(9):
    #Ler conjunto de dados
    L_altura[x]= L_altura.append(float(input(f"Altura de {x+1}°")))
    L_sexo[x]= L_sexo.append(input(f"Sexo [M/F] de {x+1}°"))
    #validacao da entrada
    if L_sexo[x] != "M" and L_sexo[x] != "F":
        print("Escolha um sexo válido! [M/F]")
        break
    #gera uma lista_m que recebe a altura dos homens e uma lista_f que recebe a altura das mulheres
    elif L_sexo[x] =="M": 
        lista_m.append(L_altura[x])
    elif L_sexo[x] == "F":
        lista_f.append(L_altura[x])
   
    
##SAÍDAS:

print(f"Sexo do individuo de maior altura: {sexo_de_maximo(L_altura, L_sexo)}")#impressao em f' -> chamada da funcao dentro de print(f'{})
print(f"Sexo do individuo de menor altura:{sexo_de_minimo(L_altura, L_sexo)}")
print(f"Média da altura de M:{media(lista_m)}")
print(f"Média da altura de F:{media(lista_f)}")
print(f"Quantidade de M:{len(lista_m)}")#tamanho da lista M
print(f"Quantidade de F: {len(lista_f)}")# tamanho da lista F
