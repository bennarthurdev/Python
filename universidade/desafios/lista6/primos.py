#leia um número
num = int(input("Número:"))
#calcule o resto da divisão do número informado por todos os números menor que ele
primo = True
for x in range(2,num,1):
    resto = num%x

    if resto == 0:
        primo = False
        print("Não é primo!")
        break
    
else:
    print("É primo")       
