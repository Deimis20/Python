# Ivedu skaiciu 5 programa atspausdina 5! = 1 * 2 * 3 * 4 * 5 = 120
import math
skaicius = int(input('Iveskite skaiciu...'))
# for i in range(0, skaicius):
#     i += 1
#     print(f'{skaicius}!= {i}')
fak = 1
print(f'{skaicius}!= ',end='')
for i in range(1, skaicius+1):
    fak = fak * i
    if i != skaicius:
        print(f'{i}',end=' * ')
    else:
        print(f'{i}',end=' ')

print(f'={fak}')