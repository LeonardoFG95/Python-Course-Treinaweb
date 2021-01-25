listaSimplesInteiro = [1, 2, 3, 8, 14, 4, 5]

print(listaSimplesInteiro[0:4])
print(listaSimplesInteiro[1:])
print(listaSimplesInteiro[:3])
novaLista = listaSimplesInteiro[:3]
print(f'novaLista = {novaLista}')

intervalo = slice(1, 4)
print(f"Slice = {listaSimplesInteiro[intervalo]}")