"""
ESERCIZIO 1 

Come già definito nella verifica precedente (versione base uguale per tutti):
primi: 5€
secondi: 4€
dal secondo primo in poi: sconto 20%
acqua gratis
bibita non acqua: +0.50€
Il programma deve stampare:
[nome] - Totale pranzo: XX.XX euro
"""

# Inserimento nome
nome = input("Inserisci il tuo nome: ")

# Liste dei piatti disponibili
primi = ['pasta', 'riso', 'pizza', 'panino']
secondi = ['bistecca', 'pesce', 'arrosto', 'braciola']
bibite = ['soda', 'aranciata', 'limonata', 'acqua']

# Raccolta ordini dell'utente
print(f"Elenco dei primi: {primi}")
ordini_primi_raw = input("Quale vuoi? Inseriscine anche più di uno. Separali con uno spazio: ").split()

print(f"Elenco dei secondi: {secondi}")
ordini_secondi_raw = input("Quale vuoi? Inseriscine anche più di uno. Separali con uno spazio: ").split()

print(f"Elenco dei bibite: {bibite}")
ordini_bibite_raw = input("Quale vuoi? Inseriscine anche più di uno. Separali con uno spazio: ").split()

# Filtraggio: si accettano solo elementi validi
ordini_primi = []
for p in ordini_primi_raw:
    if p in primi:
        ordini_primi.append(p)

ordini_secondi = []
for s in ordini_secondi_raw:
    if s in secondi:
        ordini_secondi.append(s)

ordini_bibite = []
for b in ordini_bibite_raw:
    if b in bibite:
        ordini_bibite.append(b)

# Calcolo costo primi
# Primo n.1 a 5€, dal secondo in poi sconto 20% -> 4€
if len(ordini_primi) > 1:
    totale_primi = 5 + ((len(ordini_primi) - 1) * 4)
else:
    totale_primi = len(ordini_primi) * 5

# Calcolo costo bibite
# Acqua gratis, le altre costano 0.50€
num_acque = ordini_bibite.count("acqua")
totale_bibite = (len(ordini_bibite) - num_acque) * 0.5

# Calcolo costo secondi
totale_secondi = len(ordini_secondi) * 4

# Totale finale
totale = totale_primi + totale_secondi + totale_bibite

# Output richiesto
print(f"{nome} - Totale pranzo: {totale:.2f} euro")