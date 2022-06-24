from clientes import Cliente
from bancos import Banco

from contas import conta, ContaEspecial#

joão = Cliente("João da Silva" , "3241-5599")
maria = Cliente("Maria Silva" , "7231-9955")
conta1 = conta([joão],1,1000)
conta2 = ContaEspecial([joão , maria], 2 , 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
