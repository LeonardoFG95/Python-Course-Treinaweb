from listas import lista_ligada

class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numeroCategorias = 10
        self.__tamanho = 0

        for i in range(self.__numeroCategorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    @property
    def tamanho(self):
        return self.__tamanho

    def __gerarNumeroEspalhamento(self, elemento):
        return hash(elemento) % self.__numeroCategorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        categoria.inserir(elemento)
        self.__tamanho += 1
        return True

    def remover(self, elemento):
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        categoria.removerElemento(elemento)
        self.__tamanho -= 1

    def contem(self, elemento):
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        return  categoria.contem(elemento)

    def __str__(self):
        return  self.__elementos.__str__()




# 0 (0, 50):
# 1 (50, 100):
# 2 (100, 150):
# 3 (150, 200):