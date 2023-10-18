def atvir(skaicius):
    atv = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius //= 10
        atv = atv * 10 + x1
    return atv
    
sk = int(input('Iveskite skaiciu...'))
sumaKita = atvir(sk)
print(f'Skaiciaus {sk} perrasius atcirksciai = {sumaKita}')

