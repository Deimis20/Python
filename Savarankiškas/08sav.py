b = int(input("Kiek braskiu buvo pirmaja diena: "))
d = int(input("Kiek daugiau prinoksta kiekviena diena: "))
n = int(input("Po kiek dienų norite suzinoti braskiu kieki: "))
k = 0
for i in range(1, n+1):
    k = k + b
    b = b + d
print(f'Per {n} dienas prinoko {k} braškės.')