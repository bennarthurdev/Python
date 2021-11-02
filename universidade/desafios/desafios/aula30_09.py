#entrada
n1 = int(input("Type a num: \n ->"))
n2 = int(input("Type a num: \n ->"))
#processamento
#sabemos o número de repetições(while ou for)?
## e se n1 > n2?
if (n1 > n2): ##se n1 > n2, podemos decrementar de 1 em 1 de maneira a obter esse intervalo
    for i in range(n1-1 , n2, -1):
        print(i)
else:    
    for i in range(n1+1, n2-1): # n1+1 , n1+2,..., n2-1   ##range(a1 , an , q), como q = 1, pode ser omitido.
        print(i)

vetor_i = list(range(1, 100, 1))
soma = (len(vetor_i)+(1+100))/2
