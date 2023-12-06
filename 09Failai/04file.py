def kuriam(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)


for i in range(1, 20):
    kuriam(f'09Failai\\txt\{i}byla.txt',f'{i}byloje irasyta informacija')