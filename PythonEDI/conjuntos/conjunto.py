from listas import lista_ligada
from espalhamento import tabela_espalhamento

class Conjunto():
    def __init__(self):
        self.__elementos = tabela_espalhamento.TabelaEspalhamento()

    def inserir(self, elemento):
        self.__elementos.inserir(elemento)

    #def inserirPosicao(self, posicao, elemento):
    #    if not self.contem(elemento):
    #        self.__elementos.inserirPosicao(posicao, elemento)
    #        return True
    #    return False

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    #def indice(self, elemento):
    #    return self.__elementos.indice(elemento)

    def estaVazia(self):
        return  self.__elementos.tamanho == 0

    #def recuperarElementoNo(self, posicao):
    #    return self.__elementos.recuperarElementoNo(posicao)

    #def recuperarNo(self, posicao):
    #    return self.__elementos.recuperarNo(posicao)

    #def tamanho(self):
    #    return self.__elementos.tamanho

    #def removerPosicao(self, posicao):
    #    self.__elementos.removerPosicao(posicao)

    def removerElemento(self, elemento):
        self.__elementos.remover(elemento)
