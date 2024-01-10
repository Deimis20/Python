kort = (5, 8, 9, 7, 9, 4)
kort1 = 5, 8, 9, 7, 9, 4
print(type(kort))
print(type(kort1))
print('----------')

kort2 = (2,)
kort3 = 2
print(type(kort2))
print(type(kort3))
print('----------')

list = [5, 8, 9, 7]
kort4 = tuple(list)
print(type(kort4))
print('----------')

for i in kort1:
    print(i)
print('----------')

print(kort1.count(9))
print('----------')

print(kort1.index(5))
print('----------')

k = (5, 8, 9)
g = k
print(id(g))
print(id(k))
print('----------')

k = (5, 8, 9)
a, b, c = k #ispakavimas kortedzo
g = k
print(k)
k += (5, 9)
print(id(g))
print(id(k))
print(k)
print(len(k))
print('----------')