# dalinai veikia
n = int(input('Kiek petriukas turi pazymiu...'))
suma = 0
for i in range(1, n+1):
    paz = int(input(f'Iveskite {i}-aji pazymi..'))
    if 1<=paz<=10:
        suma = suma + paz
    else:
        print('Blogas pazymus kartokite ivedima')
vid = suma / n
print(f'Petriuko vidurkis {vid}')
