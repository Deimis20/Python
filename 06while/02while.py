# ivedamas skaicius 12. Atspausdinti jo daliklius
# 1 2 3 4 6 12 ju yra 6
# 1 13 ju yra 2

sk = int(input('Iveskite skaiciu...'))
n = 1
kiek = 0
while sk >= n:
    if sk % n==0:
        print(n, end=(', '))
        kiek = kiek + 1
    n = n + 1
print(f'ju yra {kiek}')
