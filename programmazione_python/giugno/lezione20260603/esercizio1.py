"""
Autore: Alessandro Verduna
Data: 03/06/2026

Consegna: Primo Esercizio
    Scrivere un programma che, leggendo da tastiera una stringa, la salvi su file “stringa.txt”.
    Successivamente aprire il file “stringa.txt” e verificare il salvataggio.
"""

# Lettura della stringa da tastiera
stringa = input("Stringa da inserire: ")

# Apertura del file in modalità scrittura e salvataggio della stringa
with open("stringa.txt", "w", encoding="utf-8") as file:
    file.write(stringa)

# Riapertura del file in modalità lettura per verificare il contenuto
with open("stringa.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

    # Verifica del corretto salvataggio
    if contenuto == stringa:
        print("Stringa salvata correttamente")
    else:
        print("Stringa non salvata correttamente")
