#entrada
##lista de números
lista_verificacao = set()# cria um conjunto para verificação 
for x in range(26):
    lista_verificacao.add(x)#{0,1,2...26}
verificador = True
lista_numeros =[None]*10
for x in range(10):
    numero_usuario = int(input("Digite um número 0-26:"))
    verificador = numero_usuario in lista_verificacao
    if verificador != True:
        print("Digite um número válido!")
        lista_numeros[x] = "Número inválido digitado aqui!"
        break
    else:
        lista_numeros[x] = numero_usuario
print(lista_numeros)
lista_string = [' ','a' , ' b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i ' , 'j' , 'k', 'l' , 'm' , 'n'  , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' ,'w' , 'x' , 'y' , 'z']
lista_mensagem = [None]*10
for x in range(len(lista_string)):
    for y in range(len(lista_numeros)):
        if lista_numeros[y] == x:
            lista_mensagem[y] = lista_string[x]
mensagem = "".join(lista_mensagem)
print(mensagem)








