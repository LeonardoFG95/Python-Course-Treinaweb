meuDicionario = {1: 'Fabio', 2: 'Maria', 3: 'João', 4: 'José'}
meuDicionario2 = {'nome': 'João', 'sobrenome': 'Silva', 'idade': 50}

# get()
print(meuDicionario[2])
print(meuDicionario.get(2))

print(meuDicionario2.get('sobrenome'))

# len()
print(len(meuDicionario))

# pop()
meuDicionario.pop(2)
print(meuDicionario)

# clear()
#meuDicionario.clear()
print(meuDicionario)

# keys()
print(meuDicionario.keys())
print(meuDicionario2.keys())

# Adicionando Elementos
meuDicionario[5] = 'Joaquina'
print(meuDicionario)
meuDicionario2.update({'profissao': 'Programador'})
print(meuDicionario2)