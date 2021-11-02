num1 = int(input("Digite um inteiro:"))
num2 = int(input("Digite um outro inteiro:"))
quociente = 0#o quociente inicia em 0
saida_num1 = num1
if (num1>num2):
    while(num1 >= num2):
        num1 = num1 - num2
        quociente = quociente + 1
    resto = num1
elif(num2>num1):
    print("Função em construção, tente com o primeiro inteiro maior que o segundo inteiro ;)")
else:
    print("ERROR 444: Digite valores válidos!")
print(f"o quociente da divisão de {saida_num1}/{num2}= {quociente} com resto = {resto}")# num1 é exibido em sua integridade, num2 não é alterado no código e o quociente é exibido como saída ao usuário
