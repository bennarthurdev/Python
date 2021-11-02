#ler matriz 3x3
matriz = [[None]*3 for i in range(3)]
#ler matriz linha-a-linha
for i in matriz:#0,1,2
    for j in matriz:#0,1,2
        matriz[i][j] = int(input(f"m{[i+1]}{[j+1]}"))
                                                                                                                        
for i , j in matriz:#0,1,2
    matriz[1][j] = matriz[i][1]#trocar elementos linha 2 pela coluna 2

                                                                                                                      
#trocar elementos coluna 2 pela linha 2


#trocar linha-coluna
