def ivedimas():
    a = int(input('a=..'))
    b = int(input('b=..'))
    return a, b

kazkas = ivedimas()
print(kazkas)
print(type(kazkas))
x1, x2 = ivedimas()
print(f'x1 yra {x1}')
print(f'x2 yra {x2}')