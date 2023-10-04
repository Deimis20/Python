txt = 'Man labai patinka rytais anksti keltis ir eiti į mokyklą'
lt =('ąčęėįšųūžĄČĘĖĮŠŲŪŽ')
kiek = 0
for i in txt:
    print(i)
    if i in lt:
        kiek += 1 # kiek = kiek + 1
print(f'Sakinyje "{txt}" yra {kiek} LT simboliu')