m = [5, 8, 9, 7, 9, 4, -1]
print(m)
m.append(-111)
print(m)
m.insert(1, -8888)
print(m)
kiek9 = m.count(9)
print(kiek9)
m.sort(reverse=True) # .sort() didejimo tvarka .sort(reverse=True) mazejimo tvarka
print(m)
# m.reverse()
# print(m)

tekstas = ['a', 'abc', 'ab', 'acb', 'acb', 'cad', 'f']
tekstas.sort()
print(tekstas)
tekstas.sort(key=len)
print(tekstas)

tekstas.sort(key=len, reverse=True)
print(tekstas)
did = max(m)
maz = min(m)
print(m)
m.pop(2)
print(m)