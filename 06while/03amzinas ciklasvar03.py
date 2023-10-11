# amzinas ivedimas

while True:
    sk = int(input('sk=...'))
    atsakymas = input('Ar dar norite ivesti skaiciu? (T/N)')
    if atsakymas == 'T' or atsakymas == 't':
        continue                # veiksmai kuriuos norime atlikti.
    else:
        break

print('Pagaliau....') 