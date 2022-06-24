#superclass
class conta:
    def __init__(self,clientes,numero, saldo=0,):
       
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []#list to store the operations 
        self.deposito(saldo)#consideraremos o saldo inicial como um deposito
    def resumo(self):
        print(f"CC:{self.numero} ,SALDO:{self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(
                ["SAQUE" , valor]
                )
        else:
            print("Saldo insuficiente! Saque não realizado\n")

    def deposito(self , valor):
        self.saldo += valor
        self.operacoes.append(
            ["DEPÓSITO:" , valor]
        )#add dict type
    
    def extrato(self):
        for o in self.operacoes:
            print(f"{o[0]:10s} -{o[1]:10.2f}\n")
        print(f"Saldo:{self.saldo}\n")

#subclass
class ContaEspecial(conta):
    def __init__(self, clientes, numero , saldo=0, limite = 0):
        conta.__init__(self,clientes, numero, saldo) #copy the method __init__ of superclass 'conta'
        self.limite = limite #new atributtes