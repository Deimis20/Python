p = int(input('Iveskite prekiu keiki.'))
d = int(input('Kiek prekiu telpa i didele deze.'))
m = int(input('Kiek prekiu telpa i maza deze.'))
dKiek = p // d
likutis = p % d
mKiek = likutis // m
liko = likutis % m
print(f'reikes {dKiek} d.dez. ir {mKiek} m.dez. ir liks {liko} prekiu ')