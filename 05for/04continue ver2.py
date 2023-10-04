#atspausdinti visus skaicius nuo 1 iki n. jei patenka skaicius 13 ties juo sustoti.
n = int(input('n=...'))
for i in range(1, n):
    if i == 13:
        break
    print(i, end=(', '))
else:
    print('\nKiti sakiniai...')