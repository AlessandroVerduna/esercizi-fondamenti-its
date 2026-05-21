"""
ESERCIZIO 2

Input:
nome studente
intero n
carattere c
Output: scacchiera alternata con _.
In testa deve comparire una riga tipo:
Scacchiera generata da: <nome>
"""

# Input del nome
nome = input("Inserisci il tuo nome: ")

# N è la dimensione della scacchiera -> numero di righe
intero = int(input("Inserisci il valore N di dimensione della scacchiera: "))

# Carattere da alternare con _
carattere = input("Inserisci il carattere da usare nella scacchiera: ")

# Intestazione richiesta dal testo
print(f"Scacchiera generata da: {nome}\n")

# Scacchiera NxN -> ogni cella è un singolo carattere
for i in range(intero):
    riga = ""  # costruisco la riga carattere per carattere
    for j in range(intero):
        # Alternanza -> somma indici pari = carattere, dispari = _
        if (i + j) % 2 == 0:
            riga += carattere
        else:
            riga += "_"
    print(riga)