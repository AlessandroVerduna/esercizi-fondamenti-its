""" Regioni italiane """

regione = {
    "Piemonte" : ["Torino", "Asti", "Cuneo", "Alessandria"],
    "Liguria" : ["Genova", "Savona", "Imperia", "La Spezia"]
}

#print(help(regione))

chiavi = regione.keys()
valori = regione.values()

# for chiave in chiavi:
#     print(chiave)
#     print(regione.get(chiave))

# print(valori)
# print(chiavi)

for chiave, valore in regione.items():
    print(f"La regione {chiave} ha i seguenti comuni capoluoghi di provincia: {valore}")