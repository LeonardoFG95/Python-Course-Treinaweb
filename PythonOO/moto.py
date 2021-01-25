import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipoCombustivel, potencia, qtdPassageiros):
        super().__init__(cor, tipoCombustivel, potencia)
        self.qtdPassageiros = qtdPassageiros

    def abastecer(self, qtdCombustivel):
        print("O método foi chamado a partir da classe moto.")
        if self._qtdCombustivel >= 30:
            print("A moto está cheia.")
        else:
            self._qtdCombustivel += qtdCombustivel

    def pintar(self, cor):
        if cor == "Azul":
            print("A mooto não pode ser azul.")
        else:
            self._cor = cor

