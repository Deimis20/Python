# ivedamas skaicius sk. Patikrinti ar jis yra pirminis.

sk = int(input('Iveskite skaiciu...'))
n = 1
kiek = True
while sk // 2 >= n:
    n = n + 1
    if sk % n==0:
        kiek = False
        break

        
if kiek:
    print(f'Skaicius {sk} pirminis')
else:
    print(f'Skaicius {sk} sudetinis')