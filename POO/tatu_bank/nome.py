from functools import total_ordering
@total_ordering #aplica (< , > , >=, <= , == , !=)
class Nome:
    def __init__(self,nome):
        self.nome = nome # chama o método nome() em @nome.setter
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.__nome} Chave:{self.__chave}"
    def __eq__(self,  outro):
        return self.nome == outro.nome
    def __lt__(self,outro):
        return self.nome < outro.nome
    @property#
    def nome(self,valor):
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome
    @nome.setter
    def nome(self,valor): #transforma na propriedade nome
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod #cria um método estático, isto é que pode ser acessado pelo nome, sem a necessidade de um objeto
    def CriaChave(nome):
        return nome.strip().lower()
