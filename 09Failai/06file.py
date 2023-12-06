#  r w a r+ w+

def kuriam(txt):
    with open('09Failai\\data6.txt', 'w+', encoding='utf-8') as f:
        f.write('5\n')
        f.write('8\n')
        f.seek(0)
        a = int(f.readline())
        b = int(f.readline())
        s = a + b
        f.write(txt)
        f.write(f'\n {a} + {b} = {s}')
for i in range(1, 5):
    kuriam(f'{i} Rezultatas')