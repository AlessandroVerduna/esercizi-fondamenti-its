"""
    Autore: Alessandro Verduna
    Data: 03/06/2026

    Consegna: Primo Esercizio
        Scrivere un programma che, leggendo da tastiera una stringa, la salvi su file “stringa.txt”.
        Successivamente aprire il file “stringa.txt” e verificare il salvataggio.
"""

stringa = input("Stringa da inserire: ")

with open("stringa.txt", "w", encoding="utf-8") as file:
    file.write(stringa)

with open("stringa.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

    if contenuto == stringa:
        print("Stringa salvata correttamente")
    else:
        print("Stringa non salvata correttamente")