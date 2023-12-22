# név$gyártási dátum
class Auto:
    def __init__(self,sor:str):
        adatok = sor.strip().split("$")
        self.nev = adatok[0]
        self.gyarDatum = int(adatok[1])
