# pirma uzduotis atspausdinti taip:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# Antra uzduotis atspausdinti ksaicius taip:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4
# 1 2 3
# 1 2
# 1


sk = int(input('Iveskite skaiciu iki kiek....'))
for i in range(1, sk):
    for j in range(1, i+1):
        print(j, end=(' '))
    print()
for i in range(sk, 0, -1):
    for j in range(1, i):
        print(j, end=(' '))
    print()

