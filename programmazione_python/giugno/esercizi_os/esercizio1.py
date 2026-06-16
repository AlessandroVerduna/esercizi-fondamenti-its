"""
Autore: Alessandro Verduna
Data: 16/06/2026

Consegna: Primo Esercizio
    Scrivere una procedura che, dato un percorso, elenchi tutte le directories presenti.
"""

import os

def elencoDirectories(percorso):
    """
    Procedura che elenca tutte le directory presenti nel percorso indicato.

    Parametri:
        percorso (str): percorso del file system da analizzare.

    Effetti:
        Stampa a video tutte le directory contenute nel percorso.
    """
    elementi = os.listdir(percorso)

    print(f"Directory presenti in '{percorso}':")
    for elemento in elementi:
        if os.path.isdir(os.path.join(percorso, elemento)):
            print(f"- {elemento}")

elencoDirectories(".")
