aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}
aibeC = {12, 13, 14, 15}
aibeD = {-1, 1, 2, 5, 6}


# aibeA.update(aibeB)
# print(aibeA)
# print('----------')

print('Egzistuojanciu elementu salinimas, bet jei neegzistuoja elementas duoda klaida')
aibeA.remove(1)
print(aibeA)
print('----------')

print('klaidos nemeta jeigu ir neegzistuoja elementas')
aibeA.discard(2)
print(aibeA)
print('----------')


print('grazina salinama elementa')
kazkas = aibeA.pop()
print(kazkas)
print('----------')


print('aibes isvalymas ir paliekama tuscia aibe')
aibeC.clear()
print(aibeC)
print('----------')



