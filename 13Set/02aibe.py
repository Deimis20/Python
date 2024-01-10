aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}
aibeC = {12, 13, 14, 15}
aibeD = {-1, 1, 2, 5, 6}

print('Ar poaibis?')
print(aibeA.issubset(aibeB))
print('----------')


print('Ar virsaibis')
print(aibeB.issuperset(aibeA))
print('----------')



print('Ar visi skirtingi?')
print(aibeC.isdisjoint(aibeB))
print('----------')

print('Aibiu sajunga')
aibeE = aibeA.union(aibeD)
print(aibeE)
print('----------')


print('Aibiu sankirta')
aibeF = aibeD.intersection(aibeA)
print(aibeF)
print('----------')


print('Aibiu skirtumas')
aibeG = aibeA.difference(aibeD)
aibeG1 = aibeA.difference_update(aibeD) # Pasiaiskint patiems
print(aibeG)
print(aibeG1) # Pasiaiskint patiems
print('----------')

aibeG2 = aibeD.symmetric_difference(aibeC)
print(aibeG2)
print('----------')

aibeG3 = aibeC.union(aibeD)
print(aibeG3)
print('----------')