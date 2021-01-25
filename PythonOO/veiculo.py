import abc, interfaceVeiculo

class Veiculo(interfaceVeiculo.InterfaceVeiculo, abc.ABC):
    """"Essa é a classe carro. Esta classe é utilizada para instanciar novos carros no nosso programa"""

    def __init__(self, cor, tipoCombustivel, potencia):
        self._cor = cor
        self.__tipoCombustivel = tipoCombustivel
        self.__potencia = potencia
        self._qtdCombustivel = 0
        self.__isLigado = False
        self.__velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memória. :)")

    @abc.abstractmethod
    def pintar(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    def abastecer(self, qtdCombustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustivel e incrementa o atributo qtdCombustivel do objeto."""
        self._qtdCombustivel += qtdCombustivel

    def ligar(self):
        if self.__isLigado:
            print("O veículo já está ligado.")
        else:
            self.__isLigado = True
            print("O veículo foi ligado.")

    def desligar(self):
        if self.__isLigado == False:
            print("O veículo já está desligado.")
        else:
            self.__isLigado = False

    def acelerar(self, velocidade = 10):
        if self.__isLigado:
            self.__velocidade += velocidade
        else:
            print("O veículo precisa estar ligado para ser acelerado.")