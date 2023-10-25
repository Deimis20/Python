import random
n = int(input('n=...'))
sk = random.randint(0,n)
sk1 = random.randrange(1, n, 2)
sk2 = random.random()
raide = random.choice(['a', 'b', 'c'])

print("Skaicius yra:", sk)
print('Skaicius yra:', sk1)
print('Raide yra: ', raide)
print(int(sk2*100))