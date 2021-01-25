# Declaração de um set
meuSet = {1, 2, 3, 4, 1}
print(type(meuSet))

meuSet2 = set([1, 2, 8, 9, 10])
print(type(meuSet2))

# add()
meuSet.add(2)
print(meuSet)

# update()
meuSet.update([3, 4, 5, 6])
print(meuSet)

# discard()
meuSet.discard(2)
print(meuSet)

# União
print(meuSet | meuSet2)
print(meuSet.union(meuSet2))

# Interseção
print(meuSet & meuSet2)
print(meuSet.intersection(meuSet2))

# Diferença
print(meuSet - meuSet2)
print(meuSet.difference(meuSet2))

# Diferença Simetrica
print(meuSet ^ meuSet2)
print((meuSet.symmetric_difference(meuSet2)))
