from collections import  deque

minhaFila = deque(["João", "Pedro", "Augusto"])
print(minhaFila)
minhaFila.popleft()
print(minhaFila)

minhaFila.append("Maria")
print(minhaFila)
minhaFila.popleft()
print(minhaFila)