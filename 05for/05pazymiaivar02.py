
#viskas veikia

def ivedimas(nr):
    paz = int(input(f'Iveskite {nr}-aji pazymi..'))
    if 1<=paz<=10:
        return paz
    else: 
        print('Blogas pazymys kartokite ivedima')
        return ivedimas(nr)

n = int(input('Kiek petriukas turi pazymiu...'))
suma = 0
for i in range(1, n+1):
    p = ivedimas(i)
    suma = suma + p

vid = suma / n
print(f'Petriuko vidurkis {vid}')
