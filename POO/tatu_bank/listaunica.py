class ListaUnica:
    def __init__(self,elem_class):
        self.lista = []
        self.elem_class = elem_class
    def __len__(self):#retorna o tamanho do atributo lista
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self, p):#obtem o elemento no indice passado como argumento
        return self.lista[p]
    def indexValid(self , i): #retorna false caso indice seja invalido e True, caso ele exista
        return i>= 0  and i < len(self.lista)
    def add(self , elem):  
        if self.search(elem) == -1: #chama o método search e caso ele retorne -1, que significa que o elemento ainda nao existe la lista
            self.lista.append(elem)#adiciona o elemento na lista
    def remove(self, elem): #remove um elemento
        self.lista.remove(elem)
    def search(self, elem):
        self.verify_type(elem) 
        try:
            return self.lista.index(elem)
        except ValueError:
            return - 1
    def verify_type(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Tipo inválido")
    def order(self , chave=None):
        self.lista.sort(key=chave)

        
