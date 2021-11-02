n = int(input("Quantas idades serão lidas? "))
soma = 0
for x  in range(1, n+1):   #leitura das idades
    idade= int(input("Digite a idade \n ->"))##i) peça n idades 
    soma += idade
media = soma/idade
if media  >=  0 and media <= 25:
    turma = "Jovem"
elif media <= 60:
    turma = "Adulta"
else:
    turma = "Idosa"
print(turma)
