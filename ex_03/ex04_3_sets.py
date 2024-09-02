#class set

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {1, 2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_a.symmetric_difference(conjunto_c))
print(conjunto_a.issubset(conjunto_c))
print(conjunto_a. isdisjoint(conjunto_b))

conjunto_c.add(5)
print(conjunto_c)

conjunto_b.clear()
print(conjunto_b)

print(len(conjunto_a))
print(1 in conjunto_c)

