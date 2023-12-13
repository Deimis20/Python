import math

class TrikampioKlaida(Exception):
    '''Viena is trikampio klaidu'''

def trikampioPlotas(a, b, c):
    if a<=0 or b<=0 or c<=0:
        raise TrikampioKlaida('Kraštinė turi buti didesnė už 0')
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
try:
    tr2= trikampioPlotas(-2,10,10)
except TrikampioKlaida as ex:
    print(ex)
else:
    print(tr2)