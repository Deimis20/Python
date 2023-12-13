import sys


duomSar =['11GaudomKlaidas/duom1.txt','11GaudomKlaidas/duom2.txt','11GaudomKlaidas/duom 3.txt','11GaudomKlaidas/duom4.txt']
duomKlaida=[]
duomInfo=[]

try:
    for byla in duomSar:
        try:
            f = open(byla, 'r')
            duomInfo.append(f.read())
        except Exception as ex:
            duomKlaida.append(byla) 
            sys.exit()
finally:
    f = open('11GaudomKlaidas/log.txt', 'w')
    for i in duomInfo:
        f.write(i)
        f.write('\n')
    f.write(str(duomKlaida))
    print('Gal ir issaugojom kazka')
            

print(f' Klaidingi failai {duomKlaida}')
print(f'Duomenys: {duomInfo}')