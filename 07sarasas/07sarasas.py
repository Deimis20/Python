txt = '52, 14, -15, 45, 14, 58, 47, 12, 14, 12, 18, 19, 25, 12, -14, 37, 41, 58, 21, 22'
# is txt eilutes gauti lyginiu skaiciu sarasa.
# eil = txt.split(', ') skaicius duoda kaip txt
# print(eil)
sk = [int(i) for i in txt.split(', ') if int(i) % 2 == 0] # skaicius duoda kaip masyva
print(sk)
