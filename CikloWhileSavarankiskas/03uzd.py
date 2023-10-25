import random

def zaidimas():
    n = int(input("Iveskite teigiama sveiką skaicių n: "))
    if n <= 0:
        print("Ivestas skaicius turi buti teigiamas.")
        return

    generuotas_skaicius = random.randint(1, n)
    spejimu_skaicius = 0

    while True:
        spejimas = int(input(f"Atspekite sugeneruota skaiciu (nuo 1 iki {n}): "))
        spejimu_skaicius += 1

        if spejimas < 1 or spejimas > n:
            print("Netinkamas skaicius. Bandykite dar karta.")
            continue

        if spejimas == generuotas_skaicius:
            print(f"Jus atspejote! Sugeneruotas skaicius buvo {generuotas_skaicius}.")
            print(f"Atlikote {spejimu_skaicius} spejimus.")
            break
        elif spejimas < generuotas_skaicius:
            print(f"Sugeneruotas skaicius didesnis uz {spejimas}.")
        else:
            print(f"Sugeneruotas skaicius mazesnis uz {spejimas}.")

    kartoti = input("Ar norite zaisti dar karta? (T/N): ")
    if kartoti == 'T':
        zaidimas()
    else:
        print("Aciu uz zaidima.")

zaidimas()