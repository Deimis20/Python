try:
    f = open('data2.txt', 'w')
    f.write('Beleka belekur belekas')
    f.write('Beleka belekur belekas')
finally:
    f.close()

with open('data2.txt', 'a', encoding='utf-8') as f1:
    f1.write('tra ta ta')
print('Tratatata')