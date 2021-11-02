P = float(input("Digite o valor inicial:"))
Fn = P
i = float(input("Digite a taxa de juros[pontos percentuais]:"))
i = i/100 
n = 24
ipermonth = i/n
contador = 0
while contador <= n:
    J = ipermonth * Fn
    Fn = Fn + J
    contador = contador+1
J = Fn - P
print(f"O valor final será: R${Fn} a um rendimento de R${J}")
