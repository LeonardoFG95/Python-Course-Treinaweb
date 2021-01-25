import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipoCombustivel, potencia, qtdPortas):
        super().__init__(cor, tipoCombustivel, potencia)
        self.qtdPortas = qtdPortas

    def abastecer(self, qtdCombustivel):
        print("O método foi chamado a partir da classe carro.")
        self._qtdCombustivel += qtdCombustivel

    def pintar(self, cor):
        if cor == "Preto":
            print("O carro não pode ser preto.")
        else:
            self._cor = cor

