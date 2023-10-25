a = float(input('Iveskite pirmojo staciakampio ilgesne krastine...'))
b = float(input('Iveskite pirmojo staciakampio trumpesne krastine...'))

c = float(input('Iveskite antrojo staciakampio ilgesne krastine...'))
d = float(input('Iveskite antrojo staciakampio trumpesne krastine...'))

e = float(input('Iveskite treciojo staciakampio ilgesne krastine...'))
f = float(input('Iveskite treciojo staciakampio trumpesne krastine...'))

g = a * b
h = c * d
j = e * f 

if g > h:
    if g < j:
        vid = g
    elif h > j:
        vid = h
    else:
        vid = j
else:
    if h > j:
            vid = g
    elif h < j:
        vid = h
    else:
            vid = j
        
print("Vidurinis staciakampis", vid)