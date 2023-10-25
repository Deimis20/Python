def zvaigzdutes(sk):
    for skaicius in reversed(str(sk)):
        print("*" * int(skaicius))


sk = int(input("Įveskite skaičių: "))
zvaigzdutes(sk)