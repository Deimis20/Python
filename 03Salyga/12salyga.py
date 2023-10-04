#Koks 'veikiantis' p 1<=<=10
#Koks neveikiantis?

def ivedimas():
    p = int(input('p=...'))
    if not(1<=p<=10):
        print('netinkamas balas iveskite dar karta')
        return ivedimas() 
    else :
        return p

paz = ivedimas()
print(f'{paz} pazymys')