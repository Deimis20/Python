f = open('09Failai\\data1.txt', 'w')

f.write('Pirmas kartas su failu pythone. \n')
f.write(str(5))
f.close()

f1 = open('09Failai\\data1.txt', 'r', encoding='utf-8')
print(f1.readline())
f1.seek(0)
print(f1.readline())
f1.close()
