#ler vetor com cinco elementos x2
vetor_1 = [None]*5 #alocar vetor
vetor_2 = [None]*5 #alocar vetor
vetor_3 = [None]*10 #alocar o vetor
for x in range(5):#ler vetor 1 
    vetor_1[x]= int(input(f"Digite o {x + 1}° elemento do vetor 1:"))
for y in range(5): #ler vetor 2 
    vetor_2[y] = int(input(f"Digite o {y+ 1}° elemento do vetor 2:"))
print(vetor_1)
print(vetor_2)
#vetor de elementos intercalados
'''
for i in range(5):
    v3.append(v1[i])
    v3.append(v2[i])
'''
x=0
for z1 in range(9,2): #z1:0 , 2 , 4 , 6 , 8
    vetor_3[z1] = vetor_1[x]
    x+=1
y= 0
for z1 in range(1,10,2):#1 , 3 , 5, 7, 9
    vetor_3[z1] = vetor_1[y]
    y+=1
    '''
for z2 in range(1,10,2):#1, 3 , 5 , 7 , 9 
    vetor_3[z2] = vetor_2[z2]
    '''
print(f"Vetor dos elementos intercalados:{vetor_3}")
