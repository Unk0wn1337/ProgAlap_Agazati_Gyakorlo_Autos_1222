import random

print("II/A,B,C:")
randomSzamLista = []
index = 0
while index < 5:
    randomSzam = random.randint(1,100)
    randomSzamLista.append(randomSzam)
    index+=1


def masodikFeladat():
    index = 0
    while index < len(randomSzamLista):
        if index == 0:
            print(f"\t{randomSzamLista[index]}",end="")
        else:
            print(f";{randomSzamLista[index]}",end="")
        index+=1

def egyjegyuek_szama():
    egyjegyuek = 0
    index = 0
    while index < len(randomSzamLista):
        if randomSzamLista[index] < 10:
            egyjegyuek +=1
        index +=1
    return f"{egyjegyuek}"

def konzol_kiir():
    print("\nII/D,E:")
    print(f"\t Az egyjegyuek szama: {egyjegyuek_szama()}.")

def file_kiir():
    f = open("szamok.txt","w",encoding="utf-8")
    f.write("II/F:")
    f.write(f"\n\t A fejek szama: {egyjegyuek_szama()}.")
    f.close()
