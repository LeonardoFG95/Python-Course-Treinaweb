import carro, moto, veiculo

unoVermelho = carro.Carro("Vermelho", "Flex", 1.0, 4)
unoVermelho.ligar()
unoVermelho.abastecer(50)
unoVermelho.abastecer(10)
unoVermelho.acelerar(20)
unoVermelho.pintar("Preto")
print(unoVermelho.cor)
print(f"A quantidade de combustível é:")

motoVermelha = moto.Moto("Vermelha", "Gasolina", 1.0, 2)
motoVermelha.ligar()
motoVermelha.abastecer(30)
motoVermelha.abastecer(10)
motoVermelha.pintar("Azul")



