class BancoException(Exception):
    pass
class SaldoIndisponivel(BancoException):
    pass 
class ClienteNaoExiste(BancoException):
    pass
def saque (saldo, valor):
    if valor>saldo:
        raise SaldoIndisponivel
    return saldo - valor
try:
    saldo= saque(100,500)
except SaldoIndisponivel:
    print('Erro:Saldo Insuficiente!')

class EstoqueExeception(Exception):
    def __init__(self, mensagem , codigo_de_erro):
        super().__init__(mensagem)
        self.codigo_de_erro = codigo_de_erro
def verifique_quantidade(quantidade):
    if quantidade < 0:
        raise EstoqueExeception("Quantidade Negativa" , codigo_de_erro=1)
try:
    verifique_quantidade(-10)
except EstoqueExeception as ee:
    print(f"Erro:{ee.codigo_de_erro} {ee}")

