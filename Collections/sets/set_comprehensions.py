set1 = {1, 2}
set2 = {3, 4}

setComprehension = {i * i for i in range(0, 10)}
print(type(setComprehension))

setComprehension2 = {i for i in set1.union(set2)}
print(type(setComprehension2))