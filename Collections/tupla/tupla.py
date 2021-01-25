minhaTupla = (1, 2, 3, "Olá, Mundo", 1.5)
minhaTupla2 = 1, 2, 3, "Olá, Mundo", 1.5, True

print(type(minhaTupla))
print(type(minhaTupla2))

# count()
print(minhaTupla.count(1))

# index()
print(minhaTupla.index(3))

# verificar a existencia de um elemento
print(22 in minhaTupla)

print(minhaTupla.__add__(minhaTupla2))