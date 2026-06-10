"""
Autore: Alessandro Verduna
Data: 03/06/2026

Consegna: Quarto Esercizio
    Scrivere un programma che permetta di copiare il contenuto di un file in un altro file.
"""

# Apertura del file di input in modalità lettura
with open("input.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

# Apertura del file di output in modalità scrittura e copia del contenuto
with open("copia.txt", "w", encoding="utf-8") as file:
    file.write(contenuto)
