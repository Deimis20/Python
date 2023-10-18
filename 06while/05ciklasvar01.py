# ivedamas bet koks skaicius.... rasti to skaiciaus skaitmenu suma

def sumavimas(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = skaicius % 10
        sk = skaicius //10
        suma += x1
    return suma
    
sk = int(input('Iveskite skaiciu...'))
sumaKita = sumavimas(sk)
print(f'Skaiciaus {sk} skaitmenu suma = {sumaKita}')