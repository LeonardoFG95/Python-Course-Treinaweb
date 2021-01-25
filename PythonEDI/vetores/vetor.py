class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def tamanhoVetor(self):
        return len(self.__elementos)

    def __str__(self):
        # 1 2 3 4
        return ' '.join([str(i) for i in self.__elementos])

    def contem(self, elemento):
        # 1, 2, 3, 4
        # 5
        for i in range(self.tamanhoVetor()):
            elem = self.listarElemento(i)
            if elem == elemento:
                return True
        return  False

    def indice(self, elemento):
        for i in range(self.tamanhoVetor()):
            elem = self.listarElemento(i)
            if elem == elemento:
                return i
        return -1

    def inserirElementoPosicao(self, elemento, posicao):
        # 1 , 2, 3
        # 1, 2, 4, 3
        # 1, 2, 4   vetorInicio
        # 3 vetorFinal
        # 2
        vetorInicio = self.__elementos[:posicao] + [None] # 1, 2, [None]
        vetorFinal = self.__elementos[posicao:] # 3
        vetorInicio[len(vetorInicio) - 1] = elemento # 1, 2, 4 , 3
        self.__elementos = vetorInicio + vetorFinal
        self.__posicao += 1

    def inserirElementoFinal(self, elemento):
        if self.__posicao >= self.tamanhoVetor():
            # [None], [None], [None],
            self.__elementos = self.__elementos + [None]
            # [None], [None], [None], [None]
        # 1, 2, 3
        # 2
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def removerElementoIndice(self, posicao):
        # 1, 2, 3
        # 1, vetorInicio
        # 3 vetorFinal
        # 1
        vetorInicio = self.__elementos[:posicao] # 1, 2, 5 vetorInicio
        vetorFinal = self.__elementos[posicao + 1:] # 3, 1 vetorFinal
        self.__elementos = vetorInicio + vetorFinal # 1, 2, 5, 3, 1
        self.__posicao -= 1

    def removerElemento(self, elemento):
        posicao = self.indice(elemento)
        self.removerElementoIndice(posicao)

    def listarElemento(self, posicao):
        return self.__elementos[posicao]