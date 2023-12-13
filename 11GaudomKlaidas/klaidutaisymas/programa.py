def skaitom():
    with open('11GaudomKlaidas\\klaidu taisymas\\duom1.txt', 'r', encoding='utf-8') as f:
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else: 
                break
        return txt
skaitom()
tekstas = skaitom()
print(tekstas)