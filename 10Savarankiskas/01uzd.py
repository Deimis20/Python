import random
def rasom1(txt):
    with open('10Savarankiskas\\data7.txt', 'a', encoding='utf-8') as f:
        f.write(txt +"\n")


def zaidimas():
    n = int(input("Iveskite teigiama sveiką skaicių n: "))
    rasom1(f'Zaidejas ivede {n}')
    if n <= 0:
        print("Ivestas skaicius turi buti teigiamas.")
        return

    generuotas_skaicius = random.randint(1, n)
    spejimu_skaicius = 0
    zaidimai = 1
    skaicius = skaicius

    while True:
        spejimas = int(input(f"Atspekite sugeneruota skaiciu (nuo 1 iki {n}): "))
        spejimu_skaicius += 1
        if spejimas < 1 or spejimas > n:
            print("Netinkamas skaicius. Bandykite dar karta.")
            rasom1(f'Ivesti simboliai nera skaiciai')
            continue

        if spejimas == generuotas_skaicius:
            print(f"Jus atspejote! Sugeneruotas skaicius buvo {generuotas_skaicius}.")
            print(f"Atlikote {spejimu_skaicius} spejimus.")
            rasom1(f'Skaicius buvo atspetas. Atlikta buvo {spejimu_skaicius} spejimu.')
            break
        elif spejimas < generuotas_skaicius:
            print(f"Sugeneruotas skaicius didesnis uz {spejimas}.")
            rasom1(f'{spejimu_skaicius} spejimas, buvo speta, kad skaicius yra {spejimas} deja jis buvo didesnis.')
        else:
            print(f"Sugeneruotas skaicius mazesnis uz {spejimas}.")
            rasom1(f'{spejimu_skaicius} spejimas, buvo speta, kad skaicius yra {spejimas} deja jis buvo mazesnis.')

    kartoti = input("Ar norite zaisti dar karta? (T/N): ")
    
    if kartoti == 'T':
        rasom1(f'I klausima "Ar norite zaisti dar karta?" buvo atsakyta "T"')
        zaidimas()
        zaidimai += 1
        zaidimai = skaicius
    else:
        zaidimai += 1
        zaidimai = skaicius
        print("Aciu uz zaidima.")
        print(f'Buvo suzaista {zaidimai} kartu')
        rasom1(f'I klausima "Ar norite zaisti dar karta?" buvo atsakyta "N"')
        rasom1(f'Buvo suzaista {zaidimai} kartu')

zaidimas()