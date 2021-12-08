#TABELA ASCII 
CHAVE_MAXIMA = 26 # constante
'''
A funcao obterModo() garente que o usuário escolheu uma das opções possíveis e armazena a escolha na variável modo
'''
def obterModo(): 
    while True:
        print("Você quer criptografar ou descriptografar?[c/d]")
        modo = input().lower()
        if modo in "criptografar c descriptografar d".split():#separa a string em uma lista, separador padrão: barra de espaço
            return modo
        else:
            print('Escolha uma das opções: criptografar["c"] ou descriptografar ["d"] ')
'''
retorna a mensagem solicitada ao usuário.
'''
def receberMensagem():
    print("Digite sua mensagem:\n")
    return input()
'''
retorna a chave caso o usuário escolha uma válida
'''
def obterChave():
    chave = None
    while True:
        print(f"Digite uma chave numérica no intervalo:[1 - {CHAVE_MAXIMA}]")
        chave = int(input())#por padrão input retorna uma string, logo é necessário a conversão para inteiro (Typecasting)
        if( chave >=1 and chave <= CHAVE_MAXIMA):#garante uma chave válida       
            return chave

'''
Traduzir a função getTranslatedMessage()
'''
def obterTraducaoMensagem(modo,mensagem,chave):
    if modo[0] == "d":
        chave = -chave #para descriptografar é nescessário substrair a chave ao invéz de somar
    traducao = str()
    ''' 
    cada simbolo pertencente a mensagem será convertido um número e somado a chave
    '''
    for simbolo in mensagem:
        if simbolo.isalpha():#<bool>
            num = ord(simbolo)#recebe um caracter Unicode e retorna um parâmetro correspondente à tabela ASCII 
            num += chave 
            if simbolo.isupper():#<bool>    
                if num > ord('Z'):
                    num -=26 
                elif num < ord('A'):
                    num +=26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traducao += chr(num) #concatena em uma string<traducao> todos os simbolos criptografados
        else:
            traducao += simbolo #se a funcao .isalpha() retornar falso, concatena o simbolo com a string <barras de espaco>
    return traducao 
