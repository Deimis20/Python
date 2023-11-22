# petriuko pazymiia, suvedame, atspausdiname, 
# apskaiciuojame vidurki,
# mamai rodome didesnius uz 4, 
# teciui rodome didesnius uz 6
# Gavome uzsakyma visai klasei

MAMA = 4
TETIS = 6

# -------------Pazymiu kiekio funkcija-------------------
def kiekis(vardas):
    kiek = int(input(f'Kiek {vardas} turi pazymiu...'))
    return kiek
# -------------------------------------------------------
# ---------grazinanti pazymius funkcija------------------
def gautiPazymius(kiek, vardas):
    paz = []
    i = 0
    while i<kiek:
        p = int(input(f'Iveskite {vardas} {i+1}-aji pazymi...'))
        if 1<=p<=10:
            paz.append(p)
            i +=1
        else:
            print('Blogas pazymys. Kartokite ivedima.')

    return paz

# -------------------------------------------------------
# ----------------------Vidurkis-------------------------
def vidurkis(paz):
    if len(paz) == 0:
       return 0
    else:
        return sum(paz) / len(paz) 
    
# -------------------------------------------------------
# -------------------Tevu pazymiai-----------------------
def tevams(paz, kriterijus):
    tevPaz = []
    for i in paz:
        if i >= kriterijus:
            tevPaz.append(i)
    return tevPaz
# -------------------------------------------------------
# ----------------------Rezultatas-------------------------
def rezultatas(vardas):
    paz = gautiPazymius(kiekis(vardas), vardas)
    pazM = tevams(paz, MAMA)
    pazT = tevams(paz, TETIS)
    print(f'{vardas} pazymiai yra {paz}, vidurkis {vidurkis(paz)}')
    print(f'{vardas} mamai pazymiai yra {pazM}, vidurkis {vidurkis(pazM)}')
    print(f'{vardas} teciui pazymiai yra {pazT}, vidurkis {vidurkis(pazT)}')
# -------------------------------------------------------
klase = ['Petras', 'Antanas', 'Jonas', 'Martynas', 'Stasys', 'Ona']
for i in klase:


   rezultatas(i)
