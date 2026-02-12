""" Programma pitonico per gestire scontrini del bar """

import json

# menu = {
#     "Pizza": 2.5,
#     "Panino": 4.0,
#     "Bibita": 2.5,
#     "Acqua": 1.0,
#     "Caffé": 1.3
# }

with open("scontrino.json", "r", encoding="utf8") as f:
    menu = json.load(f)

scontrino = []
totale = 0

while True:
    print("----------------------MENU----------------------")
    for prodotto, prezzo in menu.items():
        print(f"{prodotto:10}: €{prezzo:.2f}")

    food = input("Aggiungi un prodotto all'elenco (q per uscire) ")

    if food.lower() == 'q':
        break
    else:
        food = food.capitalize()
        if food in menu:
            #print(food.capitalize())
            scontrino.append(food)
            totale += menu.get(food)
            #print(totale)
        else:
            print("Prodotto non disponibile")

print("---------------------------")
print("Scontrino")
print("---------------------------")
for p in scontrino:
    print(p, end = " - ")
print(f"Totale scontrino €{totale:.2f}")

print("---------------------------")
print("Programma terminato")
print("---------------------------")