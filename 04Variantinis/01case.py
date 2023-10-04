# ivedu savaites diena skaiciumi 5 paraso - penktadienis

diena = int(input("kokia savaites diena?"))
viskasok = True
match diena:
    case 1 :
        txt = 'pirmadienis'
    case 2:
        txt = 'antradienis'
    case 3:
        txt = 'treciadienis'
    case 4:
        txt = 'ketvirtadienis'
    case 5:
        txt = 'penktadienis'
    case 6:
        txt = 'sestadienis'
    case 7:
        txt = 'sekmadienis'
    case _:
        print('blogai ivesti duomenys')
        viskasok = False

if viskasok:
    print(f'{diena} - {txt}')
    
