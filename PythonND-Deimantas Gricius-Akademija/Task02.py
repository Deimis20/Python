a = float(input("Įveskite a reikšmę: "))
b = float(input("Įveskite b reikšmę: "))
k = float(input("Įveskite k reikšmę: "))
n1 = int(input("Įveskite n1 reikšmę: "))
n2 = int(input("Įveskite n2 reikšmę: "))
n3 = int(input("Įveskite n3 reikšmę: "))

if k <= a:
    sumokėtiPinigai = n1 * k
elif k > a and k < b:
    sumokėtiPinigai = n2 * k
else:
    sumokėtiPinigai = n3 * k
    
sum = round(sumokėtiPinigai, 2)
print(f'Julius už bandeles sumokės,  {sum} eurų.')

