meuDicionario = {1: 'Fabio', 2: 'Maria', 3: 'João', 4: 'José'}
print(type(meuDicionario))
meuDicionario2 = dict({1: 'Fabio', 2: 'Maria', 3: 'João', 4: 'José'})
print(type(meuDicionario2))

print(meuDicionario[4])

for chave, valor in meuDicionario.items():
    print(f" A chave é {chave} e o valor é {valor}.")