a = float(input("Iveskite pirmosios krastines ilgi: "))
b = float(input("Iveskite antrosios krastines ilgi: "))
c = float(input("Iveskite treciosios krastines ilgi: "))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("Trikampis yra lygiakrastis.")
    elif a == b or b == c or c == a:
        print("Trikampis yra lygiasonis.")
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print("Trikampis yra statusis.")
    else:
        print("Trikampis yra ivairiakrastis.")
else:
    print("Trikampio sudaryti negalima.")
