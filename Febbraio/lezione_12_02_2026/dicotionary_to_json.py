import json

menu = {
    "Pizza": 2.5,
    "Panino": 4.0,
    "Bibita": 2.5,
    "Acqua": 1.0,
    "Caffé": 1.3
}

with open("scontrino.json", "w", encoding = 'utf8') as f:
    print(json.dump(menu, f, indent = 4, ensure_ascii = False))