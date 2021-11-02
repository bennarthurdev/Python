P = int(input("Digite o valor inicial:"))
I = float(input("Digite a taxa de juros mensal:"))
n = 1
while (n <= 24):
    F = P(1+(I+n))
    print(f"No mês {n} o ganho foi {F}")
    n = n+1
