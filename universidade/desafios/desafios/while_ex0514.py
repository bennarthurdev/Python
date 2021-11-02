numero = int(input("Digite um inteiro ou 0 para sair:"))
contador = 1
soma = 0
while True:
    if numero == 0:
        break
    soma += numero
    contador += 1
media = soma/contador
print(f"Soma = {soma} Contador = {contador} ")
