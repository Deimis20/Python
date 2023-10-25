def aparatas():
    kaina = float(input("Įveskite kavos kainą (eurais)... "))
    print(f"Kava kainuos {kaina} eurų.")

    sumoketa = 0
    padirbtos = 0
    tikros = 0

    while sumoketa < kaina:
        moneta = input("Įmeskite monetą (10, 20, 50 centų arba 1, 2 eurai): ")

        if moneta not in ["10", "20", "50", "1", "2"]:
            print("Netinkama moneta. Meskite dar kartą.")
            padirbtos += 1
            continue

        verte = float(moneta)
        if verte > 2:
            verte /= 100

        sumoketa += verte
        liko = kaina - sumoketa

        if moneta in ["10", "20", "50", "1", "2"]:
            tikros += 1

        print(f"Liko sumokėti {liko:.2f} eurų.")

    graza = sumoketa - kaina

    if graza > 0:
        print(f"Grąža: {graza:.2f} eurų")
        print("Skanios kavos!")
    else:
        print("Dėkui už mokėjimą!")
        print("Skanios kavos!")
    print(f"Bandoma įmesti padirbtų monetų: {padirbtos} kartus")
    print(f"Bandoma įmesti tikrų monetų: {tikros} kartus")
aparatas()