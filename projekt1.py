"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jozef Drga
email: dodo.tn@seznam.cz
"""
from collections import Counter
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

credentials = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

meno = input ("Zadaj meno: ")
heslo = input ("Zadaj Heslo: ")
if meno in credentials and credentials[meno] == heslo:
    print ("Vitaj ", meno)
else:
    print("Nespravne meno, alebo heslo")
    quit()
print ("Zadaj cislo textu 1-3")
cislo = input()
if not cislo.isnumeric():
    print("Nespravny znak")
    quit()
cislo1 = int(cislo)

if   cislo1 not in range(1,3):
    print("Nespravne cislo textu")
    quit()

# print (cislo)

text = TEXTS[cislo1-1]
# print(text)
#texty = TEXTS.split(''',
#''')
#print(texty)
slova = text.split()

pocet_slov = len(slova)
slova_zacinajuce_velkym = 0
slova_velkymi = 0
slova_malymi = 0
cisel = 0
sucet_cisel = 0

for slovo in slova:
    if slovo[0].isupper():
        slova_zacinajuce_velkym += 1
    if slovo.isupper():  
        slova_velkymi += 1
        print (slovo)
    if slovo.islower():  
        slova_malymi += 1
    if slovo.isdigit():  
        cisel += 1
        sucet_cisel += int(slovo) 

print(f"Počet slov: {pocet_slov}")
print(f"Počet slov začínajúcich veľkým písmenom: {slova_zacinajuce_velkym}")
print(f"Počet slov písaných veľkými písmenami: {slova_velkymi}")
print(f"Počet slov písaných malými písmenami: {slova_malymi}")
print(f"Počet čísel: {cisel}")
print(f"Súčet čísel: {sucet_cisel}")

neziaduce_znaky = "!;:,.?"  

slova_ciste = [
    ''.join([char for char in slovo if char not in neziaduce_znaky])
    for slovo in slova
]


dlzky_slov = [len(slovo) for slovo in slova_ciste if slovo]


rozlozenie = Counter(dlzky_slov)


print("Graf: Počet slov podľa dĺžky písmen")
print("-" * 30)
for dlzka, pocet in sorted(rozlozenie.items()):
    print(f"{dlzka:2} písmen: {'#' * pocet} ({pocet})")