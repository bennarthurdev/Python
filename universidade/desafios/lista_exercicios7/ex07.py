frase = 0
while (frase != '1'):
    dicionario_frase = {}
    frase = input("Digite uma frase: [1 para sair]")
    y = 1
    for x  in range(len(frase)):
      if frase[x:y] in dicionario_frase:
        dicionario_frase[frase[x:y]] += 1
        dicionario_frase.update({frase[x:y]:dicionario_frase[frase[x:y]]})
      else:
        dicionario_frase.update({frase[x:y]:1})
      y+=1
    print(dicionario_frase)
    
