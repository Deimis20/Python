# suprogramuoti skaiciuotuva. veiksmai +, -, *, /, ^ - kelimas laipsniu, & - saknies traukimas.
import math;

a = int(input('Iveskite pirmaji skaiciu...'))
choice = input('Pasirinkite veiksma..')
if choice != '&':
    b = int(input('Iveskite antraji skaiciu...'))

def sudetis(a, b):
    return a + b
def atimtis(a, b):
    return a - b
def daugyba(a, b):
    return a * b
def dalyba(a, b):
    return a / b
def laipsnis(a, b):
    return a ^ b
def saknis(a):
    return math.sqrt(a)

if choice == '+':

    print(a, '+', b, '=', sudetis(a,b))
elif choice == '-':

    print(a, '-', b, '=', atimtis(a,b))
elif choice == '*':

    print(a, '*', b, '=', daugyba(a,b))
elif choice == '/':

    print(a, '/', b, '=', dalyba(a,b))
elif choice == '^':

    print(a, '^', b, '=', laipsnis(a,b))
# elif choice == '&':
#     if choice != '&':
#     print('saknis is', a, 'yra', saknis(a))






