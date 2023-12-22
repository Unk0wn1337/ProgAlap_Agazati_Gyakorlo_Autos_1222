import Auto
def harmadikFeladat():
    f = open("auto.txt","r",encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    index = 0
    autoDatumMinimum = 0
    autoDatumMinimumNev = ""
    autoSzama = 0
    while index < len(sorok):
        autoSzama += 1
        Autok = Auto.Auto(sorok[index])
        if Autok.gyarDatum > autoDatumMinimum:
            autoDatumMinimum = Autok.gyarDatum
            autoDatumMinimumNev = Autok.nev
        index+=1

    print("III/Flotta:")
    print(f"\n\tAutok szama: {autoSzama}.")
    print(f"III/Legfiatalabb: {autoDatumMinimumNev}({autoDatumMinimum})")
