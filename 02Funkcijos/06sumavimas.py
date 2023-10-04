# parasyti programa kuri sudeda du skaicius (su funkcijomis)
# 5 + 8 = 13

def ivedimas(txt):
    skaicius = int(input(f'{txt}=...'))
    return skaicius

def sumavimas():
    sk1 = ivedimas("Pirmas")
    sk2 = ivedimas("Antras")
    suma = sk1 + sk2
    return suma, sk1, sk2
    
def rezultatas():
    sum, a, b = sumavimas()
    print(f'{a} + {b} = {sum}')

rezultatas()