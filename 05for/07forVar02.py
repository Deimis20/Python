# atspausdinti visus penkiazenklius skaicius kuriu skaitmenu suma lygi skaitmenu sandaugai
# suskaiciuoti kiek ju yra....
# nuo 10000 iki 99999
kiek = 0
for i in range(10000, 100000):
    sum = 0
    sd = 1
    sk = i
    for j in range(5):
        x1 = sk % 10
        sk = sk // 10
        sd = sd * x1
        sum = sum + x1
    if sum == sd:
        print(i,end=', ')
        kiek += 1
print(f'ju yra {kiek}')

