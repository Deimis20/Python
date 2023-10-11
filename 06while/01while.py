# while salyga:
#     veiksmas kol salyga teisinga
#     sbarbu ... turi buti keiciama salygos reiksme!!!
# else:
#     ciklas tikrai pilnai ivyko....

# kiti sakiniai

# atspausdinti skaicius nuo 1 iki n
n = int(input('n=....'))
sk = 1
while sk != n+1 :
    if sk == 13:
        break
    print(sk, end=(', '))
    sk = sk + 1

else:
    print('ciklas tikrai pilnai ivyko....')
print('Programa baigia darba')
