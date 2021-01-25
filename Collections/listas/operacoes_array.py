from array import  array

array1 = array('B', [1, 2, 3, 4, 5, 6])
print(f'Array1 = {array1}')

#for i in array1:
#   print(i)

print(array1)

# Inserindo elementos
array1.insert(2, 50)
print(array1)

# Removendo elementos
array1.remove(4)
print(array1)

# Buscar elemento
print(array1.index(50))