listaSimplesInteiro = [1, 2, 3, 8, 14, 4, 5]
listaSimplesString = ["Olá", "Mundo"]
listaSimplesMesclada = [1, 2, 3, "Olá", "Mundo", True, 1.5]
nestedList = [[1, 2, True], ["Ola", "Mundo"]]

print(listaSimplesInteiro)
print(nestedList)

#Len()
print(len(listaSimplesInteiro))
print(len(nestedList))

#Append()
listaSimplesInteiro.append(8)
print(listaSimplesInteiro)

#Insert()
listaSimplesInteiro.insert(2, "Olá")
print(listaSimplesInteiro)

#Remove()
listaSimplesInteiro.remove("Olá")
print(listaSimplesInteiro)

#Index()
index = listaSimplesInteiro.index(3)
print(index)

#Count()
count = listaSimplesInteiro.count(3)
print(count)

#Sort
listaString = ["A", "B", "C"]
listaString.sort(reverse=True)
print(listaString)
