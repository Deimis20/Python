kiek=0
for i in range(1000,10000):
    du=i//100
    pdu=i%100
    suma=du+pdu
    kdu=suma**2
    if kdu==i:
        print(i,end=(', '))
        kiek+=1
print(f'yra {kiek} skaiciai.')