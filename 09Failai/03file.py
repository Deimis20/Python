# Sukuriama kelios eilutes sarasu. Nuskaityti ir sudeti i atskirus sarasus

def kuriam():
    with open('09Failai\\data3.txt', 'w', encoding='utf-8') as f:
        f.write('10 25 14 25 47 36\n')
        f.write('1 5 4 8\n')
        f.write('5 8 7 6 9 5 44 1 2 5\n')
        f.write('\n')
        f.write('5 8 7 6 9 5 44 1 2 5\n')
        f.write('\n')
        f.write('0\n')
        f.write('\n')
        f.write('5 8 7 6 9 5 44 1 2 5\n')
def skaitom():
    with open('09Failai\\data3.txt', 'r', encoding='utf-8') as f:
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else: 
                break
        return txt
kuriam()
visas = skaitom()
# print(visas)
skaiciai = []
for eil in visas:
    eilSk = [int(x) for x in eil.split(' ') if x != "\n"]
    if len(eilSk) > 0:
        skaiciai.append(eilSk)
print(skaiciai)
print(skaiciai[0])