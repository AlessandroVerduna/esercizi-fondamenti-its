"""
ESERCIZIO 7

Chiedere:
nome studente
numero di ore utilizzo VM
costo orario (float)
Calcolare costo totale.
Se ore > 100 applicare sconto 10%.
Output:
<nome> - costo totale VM: XX.XX euro
"""

# Input nome -> usato nell'output finale
nome = input("Nome dello studente: ")

# Input ore di utilizzo -> intero
ore_vm = int(input("Inserire numero di ore di utilizzo della VM: "))

# Input costo orario -> float
costo_orario = float(input("Costo orario della VM: "))

# Calcolo costo totale -> sconto 10% se ore > 100
if ore_vm > 100:
    costo_totale = (costo_orario * ore_vm) * 0.9
else:
    costo_totale = costo_orario * ore_vm

# Output richiesto dal testo
print(f"{nome} - costo totale VM: {costo_totale:.2f} euro")