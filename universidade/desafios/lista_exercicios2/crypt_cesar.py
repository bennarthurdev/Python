def cod_cesar(texto , chave):
    min = 32
    max = 126
    crypt = None
    sum_texto_chave = ord(texto) + chave
    
    if ord(texto) > max or ord(texto) < min:
        print("Digite um caractere válido!")
        
    elif  sum_texto_chave > 126:
        sobra = sum_texto_chave % 126
        crypt = sobra + (min-1)
        print(chr(crypt))
        
    else:
        #crypt = sum_texto_chave
        chr_crypt = chr(sum_texto_chave)
        print(chr_crypt)
    
def decod_cesar(texto, chave):
        min = 32
        max = 126        
        decrypt = None
        sub_texto_chave = ord(texto)  - chave
        decrypt = chr(sub_texto_chave)
        print(decrypt)
         
txt = input("Caractere:")
chv =int(input("Chave:"))
cod_cesar(txt,chv)
decod_cesar(txt,chv)



