#ler vetor com cinco elementos x2
vetor_1 = [None]*5 #alocar vetor
vetor_2 = [None]*5 #alocar vetor
for x in range(5):#ler vetor 1 
    vetor_1[x]= int(input(f"Digite o {x + 1}° elemento do vetor 1:"))
for x in range(5): #ler vetor 2 
    vetor_2[x] = int(input(f"Digite o {x + 1}° elemento do vetor 2:"))
print(vetor_1)
print(vetor_2)
#vetor de elementos intercalados
vetor_3 = vetor_1 + vetor_2
print(f"Vetor dos elementos intercalados:{vetor_3}")
