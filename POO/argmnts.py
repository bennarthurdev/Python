class Televisao:
    '''
    magic method - receive 4 positional arguments
    
    self - 
    '''
    def __init__(self ,start, min = 2 , max = 14):#constructor args
        self.ligada = False 
        self.canal = start 
        self.cmin = min #1
        self.cmax = max # 99
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin: #canal atual >= 1
            self.canal -= 1  #decrementa canal
        else:
            self.canal = self.cmax
    def munda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax: # canal atual <= 99
            self.canal += 1 #incrementa canal
        else:
            self.canal = self.cmin
minimo = Televisao()

