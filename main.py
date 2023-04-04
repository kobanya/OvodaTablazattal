'''
NB-2023.04.05

Mindent óvodás adatait generáljuk vagy véletlenszerűen választhuk ki és táblázatba írjuk ki
'''

import random
from tabulate import tabulate

def gyerek_adatok(beker_szam):
    szem_minta = ['zöld', 'kék', 'barna', 'szürke'] # ezekből választ a véletlen generátor
    haj_minta = ['barna', 'szőke', 'fekete', 'vörös'] # ezekből választ a véletlen generátor
    keresztnevek = ['Béla', 'Sára','Zoltán', 'Györgyi', 'Juli','Zsóka', 'Jenő', 'Gábor', 'Gergő', 'Tamás', 'Nóra', 'Napsugár', 'Szabolcs', 'Szilvia']
    adatok = [] # üres lista az adatoknak
    for i in range(beker_szam):
        nev = random.choice(keresztnevek)  # bekérés
        ev = random.randint(3, 6) # véletlen generátor
        magassaga= random.randint(90,130) # véletlen generátor
        sulya= random.randint(20,45) # véletlen generator
        szeme = random.choice(szem_minta) #véletlen választás
        haja = random.choice(haj_minta) #véletlen választás
        adatok.append([i+1, nev, ev, szeme, haja,magassaga,sulya]) # adatok hozzáadása a listához
    return adatok

beker_szam = int(input("Hány gyerek adatát szeretné generálni: "))
adatok = gyerek_adatok(beker_szam) #meghívás

print('')
print(tabulate(adatok, headers=["Sorszám", "Név", "Életkor", "Szemszín", "Hajszín", "Magassága","Testsúlya"], tablefmt="pipe")) # táblázat nyomtatása
print('')
