import criptography 

modo = criptography.obterModo()
mensagem = criptography.receberMensagem()
chave = criptography.obterChave()

print("A tradução da sua mensagem é:")
print(criptography.obterTraducaoMensagem(modo,mensagem,chave))
