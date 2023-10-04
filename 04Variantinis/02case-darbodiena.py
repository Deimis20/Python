diena = int(input("kokia savaites diena?"))
viskasok = True
match diena:
    case 1 | 2 | 3 | 4 | 5:
        txt = 'Darbo diena'
    case 6 | 7:
        txt = 'Savaitgalis'
    case _:
        print('blogai ivesti duomenys')
        viskasok = False

if viskasok:
    print(f'{diena} - {txt}')