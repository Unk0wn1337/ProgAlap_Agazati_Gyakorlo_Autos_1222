import Auto
f = open("auto.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()
def flotta():
    index = 0
    while index < len(sorok):
        index+=1
    return f"III/Flotta\n\tAutok szama: {index}."

def legfiatalabbAuto():
    AutoLegFiatalabb = 2000
    AutoLegFiatalabbNeve = ""
    index = 0
    while index < len(sorok):
        Autok = Auto.Auto(sorok[index])
        if Autok.gyarDatum > AutoLegFiatalabb:
            AutoLegFiatalabb = Autok.gyarDatum
            AutoLegFiatalabbNeve = Autok.nev
        index+=1
    print(f"III/Legfiatalabb\n\tA legfiatalabb auto: {AutoLegFiatalabbNeve}({AutoLegFiatalabb}).")


