viniesIlgis = float(input('Kokio ilgio vinis cm?...'))
kalGylis = float(input('Kiek stalius ikala vienu smugiu cm?...'))

smugis =  0
for i in range (int((viniesIlgis/kalGylis)+1)):
        viniesIlgis = viniesIlgis - kalGylis
        smugis += 1
        if viniesIlgis > 0:
            print(f'Tuk!{smugis} smugis, {round(viniesIlgis,2)} liko neikaltos')
        else:
            print(f'Tuk!{smugis} smugis, vinis ikalta.')
            break

    