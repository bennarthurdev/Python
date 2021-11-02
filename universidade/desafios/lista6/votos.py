n = int(input("Número de eleitores:"))#peça o numero total de eleitores
votos_joao = 0
votos_jose = 0
votos_maria = 0
for x in range(1 , n):
    voto = int(input("Escolha seu candidato \nJoão - 5555 \nJose-4444\nMaria-3333\nSeu Voto:"))#leia os votos
    if voto == 5555:
        votos_joao =+ 1
        print(votos_joao)
    elif voto == 4444:
        votos_jose =+ 1
    elif voto == 3333:
        votos_maria =+1
    else:
        print("Escolha um candidato válido!")
print(f"João = {votos_joao}\nJosé = {votos_jose}\nMaria= {votos_maria}")
