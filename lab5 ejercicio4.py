l1 = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]
l2 = [('one', 1), ('two', 2), ('six', 6)]
#a
s1 = set(l1)
s2 = set(l2)
#b
s3 = s1.intersection(s2)
#c
s4 = s1.symmetric_difference(s2)
#d
l3 = sorted(list(s3.union(s4)), key = lambda x: x[1])
print('lista de elementos de s3 y s4, ordenados por el numero entero de cada tupla:', l3)
