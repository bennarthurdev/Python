import pygame
import random

pygame.init()
white = (255,255,255) 
pink = (255,200,200)
green = (0,255,0)
black = (0,0,0)
preto = (0,0,0)
red = (255,0,0)
amarelo =(255,255,0)
screen = pygame.display.set_mode((1200,400))
pygame.display.set_caption("GEOBINGO")
screen.fill(white)

#fonte no começo
fonte = pygame.font.SysFont(None , 50)

#bingo
pygame.draw.rect(screen,green,(400,0,400,400),0)

#bolas
def bolinhas(nivel,p,linhas):
    neg=[1,-1]
    for z in range(nivel):
        for x in neg:
            pygame.draw.circle(screen,white,(600,(170-139*p)+(1-2*p)*(-10*z)),5)
            if z<4-linhas:
                pygame.draw.circle(screen,white,(600+9.9744*x,(170-139*p)+(1-2*p)*(-10*z-0.715)),5)
            if z<3-linhas:
                pygame.draw.circle(screen,white,(600+9.9744*x+9.77*x,(170-139*p)+(1-2*p)*(-10*z-0.715-2.13)),5)
            if z<2-linhas:
                pygame.draw.circle(screen,white,(600+9.9744*x+9.77*x+9.3667*x,(170-139*p)+(1-2*p)*(-10*z-0.715-2.13-3.502)),5)
            if z<1-linhas:
                pygame.draw.circle(screen,white,(600+9.9744*x+9.77*x+9.3667*x+8.771*x,(170-139*p)+(1-2*p)*(-10*z-0.715-2.13-3.502-4.8022)),5)

bolinhas(3,0,0)

def bolinhas_aleatorias():
    for z in range(4):
        for w in range(4):
            x  = random.randint(0,55)
            y  = random.randint(0,45)
            pygame.draw.circle(screen,white,(545 + x + (z%2)*55,55 + y + (z//2)*45),5)

def roleta(giro):
    #esfera
    pygame.draw.circle(screen,amarelo,(600,100),75,1)
    for x in range(4):
        pygame.draw.ellipse(screen,amarelo,(540+(x*15),25,120-(x*30),150),1)#surface, color, rect, width=0
    pygame.draw.line(screen,amarelo,(600,25),(600,175))#surface, color, start_pos, end_pos, width=1
    pygame.draw.line(screen,amarelo,(525,100),(675,100))


    #saida
    #pygame.draw.line(screen,amarelo,(585,173.48 - 146.96*giro),(585,200 - 200*giro))
    #pygame.draw.line(screen,amarelo,(615,173.48 - 146.96*giro),(615,200 - 200*giro))
    pygame.draw.rect(screen,amarelo,(585,173.48 - 173.48*giro,30,200-173.48),0)
    
    #manivela
    pygame.draw.line(screen,amarelo,(677,100),(685,100),3)
    pygame.draw.line(screen,amarelo,(685,100),(685,50+giro*100),3)
    pygame.draw.line(screen,amarelo,(685,50+giro*100),(700,50+giro*100),3)
    pygame.draw.line(screen,red,(700,50+giro*100),(750,50+giro*100),5)
    pygame.draw.line(screen,red,(700,45+giro*100),(700,55+giro*100),3)
    #laterais
    pygame.draw.line(screen,red,(522,85),(522,200),5)
    pygame.draw.line(screen,red,(677,85),(677,200),5)

roleta(0)

def roleta_angulo(giro):
    #bolinha
    bolinhas_aleatorias()
    bolinhas(1,0,2)
    bolinhas(1,1,2)
    
    #esfera
    pygame.draw.circle(screen,amarelo,(600,100),75,1)
    pygame.draw.line(screen,amarelo,(600,25),(600,175))#surface, color, start_pos, end_pos, width=1
    pygame.draw.line(screen,amarelo,(525,100),(675,100))
    negat=[1,-1]
    for x in negat:
        pygame.draw.line(screen,amarelo,(600+(23.17627*x),25+3.67076),(600-(23.17627*x),175-3.67076))
        pygame.draw.line(screen,amarelo,(525+3.67076,100+(23.17627*x)),(675-3.67076,100-(23.17627*x)))
        
        pygame.draw.line(screen,amarelo,(600+(23.17627*x)+20.90762*x,25+3.67076+10.65296),(600-(23.17627*x)-20.90762*x,175-3.67076-10.65296))
        pygame.draw.line(screen,amarelo,(525+3.67076+10.65296,100+(23.17627*x)+20.90762*x),(675-3.67076-10.65296,100-(23.17627*x)-20.90762*x))
    pygame.draw.circle(screen,green,(600,100),76,1)
    #saida
    if giro%2 == 1:
        pygame.draw.circle(screen,red,(600,100),30,0)
        pygame.draw.circle(screen,amarelo,(600,100),30,1)
        pygame.draw.circle(screen,amarelo,(600,100),7,0)

    #manivela
    pygame.draw.line(screen,amarelo,(677,100),(700,100),3)
    pygame.draw.line(screen,red,(700,100),(750,100),5)
    pygame.draw.line(screen,red,(700,95),(700,105),3)
    
    #laterais
    pygame.draw.line(screen,red,(522,85),(522,200),5)
    pygame.draw.line(screen,red,(677,85),(677,200),5)

#espaço para começar
fonte_do_espaco = pygame.font.SysFont(None , 50)
texto = fonte_do_espaco.render(("APERTE ESPAÇO"), False, black)
screen.blit(texto, (450,270))
texto = fonte_do_espaco.render(("PARA RODAR"), False, black)
screen.blit(texto, (485,325))

    

#primeira cartela
def cartela(xx):
    pygame.draw.rect(screen,black,(200+xx,50,100,300),1)
    pygame.draw.rect(screen,black,(100+xx,150,300,100),1)
    pygame.draw.rect(screen,black,(100+xx,50,300,300),1)
    pygame.draw.rect(screen,black,(xx,0,400,50),1)
    pygame.draw.rect(screen,black,(xx,50,100,300),1)
    pygame.draw.rect(screen,black,(xx,350,400,50),1)
    #quadrado(100,100) começa(100,50)
    #escrita
    texto = fonte.render(("CARTELA"), False, black)
    screen.blit(texto, (120+xx,13))

    texto = fonte.render(("PONTOS :"), False, black)
    screen.blit(texto, (50+xx,363))

cartela(0)
cartela(800)


#dessenho dos pontos
def desenhar_quadrado(cartela,posição):
    posição = posição/100
    pygame.draw.rect(screen,black,(25+cartela,75+150*posição,50,50))
    pygame.draw.rect(screen,white,(30+cartela,80+150*posição,40,40))
    fonte1 = pygame.font.SysFont(None , 20)
    texto = fonte1.render(("QUADRADO"), False, black)
    screen.blit(texto, (10+cartela,150+150*posição))
def desenhar_triangulo(cartela):
    posição=0
    pygame.draw.rect(screen,black,(25+cartela,75+150*posição,50,50))
    pygame.draw.polygon(screen,white,[(25+cartela,75+150*posição),(75+cartela,75+150*posição),(75+cartela,125+150*posição)])
    fonte1 = pygame.font.SysFont(None , 20)
    texto = fonte1.render(("TRI NGULO"), False, black)
    screen.blit(texto, (10+cartela,150+150*posição))
def desenhar_losango(cartela):
    posição=0
    pygame.draw.polygon(screen,black,[(50+cartela,75+150*posição),(75+cartela,100+150*posição),(50+cartela,125+150*posição),(25+cartela,100+150*posição)])
    pygame.draw.polygon(screen,white,[(50+cartela,80+150*posição),(70+cartela,100+150*posição),(50+cartela,120+150*posição),(30+cartela,100+150*posição)])
    fonte1 = pygame.font.SysFont(None , 20)
    texto = fonte1.render(("LOSANGO"), False, black)
    screen.blit(texto, (10+cartela,150+150*posição))




def numeros(nlista):
    list = [None]*nlista
    for x in range(len(list)):
        comparador = None
        while comparador in list:
            comparador  = random.randint(1,30)
        list[x]=comparador
    list2=[]
    for num in list:
        stn = str(num)
        if num<10:
            stn= "0"+stn
        list2.append(stn)
    return(list2)

def escreve_numeros(xx,list2):
    x , y = 130 + xx,80
    for j in range(3):
        for i in range(3):
            texto = fonte.render((list2[j*3 + i]), False, black)
            screen.blit(texto, (x + 100*i, y + 100*j))

    pygame.display.update()



lista1 = numeros(9)
lista2 = numeros(9)
escreve_numeros(0,lista1)
escreve_numeros(800,lista2)
lista3 = numeros(15)



def marcar(xx,posição,numero):
    pygame.draw.circle(screen,red,(150+xx+((posição%3)*100),100+((posição//3)*100)),40)
    tamanho = pygame.font.SysFont(None , 50)
    texto = tamanho.render((numero), False, black)
    screen.blit(texto, (130+ xx+ ((posição%3)*100), 80 + ((posição//3)*100)))

#CONTADOR DE PONTOS
#VERIFICA SE O USUARIO FEZ UM QUADRADO
def fez_quadrado(lista , fez_quadrado = False):# return <bool>
    if lista[0]=="x" and lista[1]=="x" and lista[2]=="x" and lista[3]=="x" and lista[4] != "x" and lista[5]=="x" and lista[6] =="x" and lista[7] == "x" and lista[8] == "x":
        fez_quadrado= True
    return fez_quadrado
#VERIFICA SE O USUARIO FEZ UM TRIANGULO
def fez_triangulo(lista, fez_triangulo = False): #return <bool>
    bool_list = [lista[0] == "x" and lista [1] != "x" and lista[2] != "x" and lista[3] == "x" and lista[4] == "x" and lista[5] != "x" and lista[6] == "x" and lista[7] == "x" and lista[8] == "x" , lista[0] == "x" and lista[1] == "x" and lista[2] == "x" and lista[3] == "x" and lista[4] == "x" and lista[5] != "x" and lista[6] == "x" and lista[7] != "x" and lista[8] != "x" , lista[0]== "x" and lista[1] == "x" and lista[2] == "x" and lista[3] != "x" and lista [4] == "x" and lista[5] == "x" and lista[6] != "x" and lista[7] != "x" and lista[8] =="x", lista[0] !="x" and lista[2] == "x" and lista[4] == "x" and lista[5] == "x" and lista[6] =="x" and lista[7]=="x" and lista[8] == "x"  and lista[1] != "x" and lista[3] != "x"]
    for x in bool_list:
        if x:
            fez_triangulo = True
    return fez_triangulo
#VERIFICA SE O USUARIO FEZ UM LOSANGO return <bool>
def fez_losango(lista, fez_losang=False,cont=0):                              
    if lista[0]!="x" and lista[1]=="x" and lista[2]!="x" and lista[3]=="x" and lista[4] != "x" and lista[5]=="x" and lista[6] !="x" and lista[7] == "x" and lista[8] != "x":
        fez_losang = True
    return fez_losang

pontos={"pontos1":0,"pontos2":0}

#VERIFICA SE O USUÁRIO FEZ A TABELA TODA
def prencheu_cartela(lista, cont = 0, prencheu_cartela = False):
    for x in lista:
        if x == "x":
            cont +=1
    if cont == 9:
        prencheu_cartela = True
    return prencheu_cartela

#incrementar os pontos feitos na rodada
def pontuar(lista , pontos,xx):
    if fez_quadrado(lista) and pontos<200:
        desenhar_quadrado(xx,pontos)
        pontos += 200
    if fez_triangulo(lista) and pontos<150:
        pontos += 150
        desenhar_triangulo(xx)
    if fez_losango(lista)  and pontos<100:
        desenhar_losango(xx)
        pontos += 100
    if prencheu_cartela(lista):
        pontos = 500        
    return pontos
#VERIFICA QUEM FEZ A MAIOR PONTUACAO
def vencedor(pontos1,pontos2):
    fonte = pygame.font.SysFont(None , 50)
    if pontos1 == pontos2:
        texto = fonte.render(("EMPATE"), False, black)
        screen.blit(texto, (455,340))
    if pontos1 > pontos2:
        print("Jogador 1 venceu!")
        texto = fonte.render(("JOGADOR 1 VENCEU!"), False, black)
        screen.blit(texto, (425,340))
    if pontos1 < pontos2:
        print("Jogador 2 venceu!")
        texto = fonte.render(("JOGADOR 2 VENCEU!"), False, black)
        screen.blit(texto, (425,340))
 
#FINAL CONTADOR DE PONTOS
def escrever_pontos(pontos,xx):
    pygame.draw.rect(screen,white,(250+xx,351,149,48))
    pontostr = str(pontos)
    fonte = pygame.font.SysFont(None , 50)
    texto = fonte.render((pontostr), False, black)
    screen.blit(texto, (250+xx,363))

escrever_pontos(0,0)
escrever_pontos(0,800)

turno=1
giradas = 0
jogo = True
while jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogo = False


            
        if (evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE):
            if giradas == 0:
                pygame.draw.rect(screen,green,(450,250,300,150))

            if giradas<15:
                pygame.draw.circle(screen,green,(600,300),50)

                pygame.mixer.music.load('roleta_som.wav')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(1)

                for nada in range(10):
                    
                    pygame.draw.rect(screen,green,(400,0,400,200),0)
                    roleta_angulo(turno)
                    pygame.display.update()
                    pygame.time.delay(250)

                    
                    pygame.draw.rect(screen,green,(400,0,400,200),0)
                    bolinhas_aleatorias()
                    bolinhas(1,0,2)
                    bolinhas(1,1,2)
                    roleta(turno%2)
                    pygame.display.update()
                    pygame.time.delay(250)
                    
                    turno+=1

                pygame.mixer.music.stop()
                
                pygame.mixer.music.unload()
                
                pygame.mixer.music.load('bola_sai.wav')
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(1)
                
                pygame.time.delay(100)
                
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.draw.rect(screen,green,(400,0,400,200),0)
                bolinhas(3,0,0)
                roleta(0)
                pygame.display.update()

                #numero
                pygame.draw.circle(screen,white,(600,300),50)
                fonte = pygame.font.SysFont(None , 100)
                texto = fonte.render((lista3[giradas]), False, black)
                screen.blit(texto, (560,270))
                pygame.display.update()
                if lista3[giradas] in lista1:
                    local = lista1.index(lista3[giradas])
                    marcar(0,local,lista1[local])
                    lista1[local]="x"
                if lista3[giradas] in lista2:
                    local = lista2.index(lista3[giradas])
                    marcar(800,local,lista2[local])
                    lista2[local]="x"
            if giradas > 2:
                pontos1x = pontuar(lista1 , pontos["pontos1"] , 0)
                if pontos1x > pontos["pontos1"]:
                    pontos["pontos1"] = pontos1x
                    escrever_pontos(pontos1x,0)
                
                
                pontos2x = pontuar(lista2 , pontos["pontos2"] , 800)
                if pontos2x > pontos["pontos2"]:
                    pontos["pontos2"] = pontos2x
                    escrever_pontos(pontos2x,800)

                if(pontos["pontos1"] >= 500) or (pontos["pontos2"] >= 500):
                    giradas = 14
                
            giradas +=1
            if giradas==15:
                pygame.time.delay(2500)
                pygame.draw.circle(screen,green,(600,300),50)
                fonte = pygame.font.SysFont(None , 100)
                texto = fonte.render(("ACABOU"), False, black)
                screen.blit(texto, (455,270))
                vencedor(pontos["pontos1"],pontos["pontos2"])
                

            if giradas>15:
                x=1


            

    pygame.display.update() 



pygame.quit() 

