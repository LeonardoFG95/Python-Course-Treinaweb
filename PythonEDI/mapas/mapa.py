from listas import lista_ligada
from mapas import assosiacao

class Mapa():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numeroCategorias = 10

        for i in range(self.__numeroCategorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    def gerarNumeroEspalhamento(self, chave):
        return hash(chave) % self.__numeroCategorias

    def contemChave(self, chave):
        numeroEspalhamento = self.gerarNumeroEspalhamento(chave)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperarElementoNo(i)
            if associacao.chave == chave:
                return True
        return False

    def remover(self, chave):
        numeroEspalhamento = self.gerarNumeroEspalhamento(chave)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperarElementoNo(i)
            if associacao.chave == chave:
                categoria.removerElemento(associacao)
                return True
            return False

    def adicionar(self, chave, valor):
        if self.contemChave(chave):
            self.remover(chave)
        numeraEspalhamento = self.gerarNumeroEspalhamento(chave)
        categoria = self.__elementos.recuperarElementoNo(numeraEspalhamento)
        categoria.inserir(assosiacao.Associacao(chave, valor))

    def recuperar(self, chave):
        numeroEspalhamento = self.gerarNumeroEspalhamento(chave)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperarElementoNo(i)
            if associacao.chave == chave:
                return associacao.valor
        return False

    def __str__(self):
        temp = self.__elementos.__str__()
        return temp




