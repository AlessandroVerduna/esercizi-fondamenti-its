""" Strutture dati in Python """

# Questa è una LISTA e può avere diversi tipi di dati e anche dati duplicati
citta_1 = ["Torino", "Milano", "Roma", "Cumiana"]

# Questa è una TUPLA e quando la creo non posso più modificarla; è immutabile
citta_2 = ("Torino", "Milano", "Roma", "Cumiana")

# Questo è un SET e NON ammette duplicati, contenitore NON ordinato. Non mi da errore ma smplicemente non la aggiunge
citta_3 = {"Torino", "Milano", "Roma", "Cumiana", "Torino"}

# Mi da il tipo della variabile
print(type(citta_3))

# Mi elenca tutto quello che posso fare con quest classe
#print(dir(citta_3))

# Aggiunge un elemnto alla fine
citta_1.append("Genova")

# Mi stampa quello che c'è tra tonde
print(citta_1)

# Mi cancella un elemento dalla lista che di default è l'ultimo
citta_1.pop(0)
print(citta_1)

# Con la funzione add() posso aggiungere degli elementi a un set{} ; cosa che non posso fare con append()
citta_3.add("Piossasco")

# Questo è un dictionary ovvero una coppia CHIAVE-VALORE
regioni = {
    "Piemonte": ["Torino", "Alessandria"],
    "Liguria": ["Genova", "Rapallo"],
    "Lombardia": ["Milano", "Como"]
}

# for regione, comuni in regioni.items():
#     for citta in comuni:
#         print(f"La regione {regione} ha i seguenti comuni: {citta}")

# for regione, comuni in regioni.items():
#     print(f"La regione {regione} ha i seguenti comuni: {comuni}")

# for regione in regioni.keys():
#         print(f"La regione {regione} ha i seguenti comuni: {regioni.get(regione)}")    


# for regione in regioni.keys():
#         print(f"La regione {regione} ha i seguenti comuni: {regioni[regione]}")    

for regione in regioni.keys():
    for comuni in regioni.get(regione):
        print(comuni)

# print(regioni)
# print(dir(regioni))