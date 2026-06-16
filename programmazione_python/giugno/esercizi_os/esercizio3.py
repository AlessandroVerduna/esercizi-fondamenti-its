"""
Autore: Alessandro Verduna
Data: 16/06/2026

Consegna: Terzo Esercizio
    Scrivere un programma Python per eseguire un comando del sistema operativo
    usando il modulo os.
"""

import os

def eseguiComando(comando):
    """
    Procedura che esegue un comando del sistema operativo.

    Parametri:
        comando (str): comando da eseguire nel terminale.

    Effetti:
        Esegue il comando e mostra l'output a video.
    """
    os.system(comando)

comando_input = input("Inserisci un comando da eseguire: ")
eseguiComando(comando_input)
