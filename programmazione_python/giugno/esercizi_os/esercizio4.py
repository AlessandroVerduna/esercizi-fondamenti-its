"""
Autore: Alessandro Verduna
Data: 16/06/2026

Consegna: Quarto Esercizio
    Scrivere un programma che elimini tutti i files che contengono nel nome
    una sequenza di caratteri data in input.
"""

import os

def eliminaFiles(percorso, sequenza):
    """
    Procedura che elimina tutti i file presenti nel percorso indicato
    che contengono nel nome la sequenza di caratteri specificata.

    Parametri:
        percorso (str): percorso della cartella da analizzare.
        sequenza (str): sequenza di caratteri da cercare nel nome dei file.

    Effetti:
        Elimina i file che contengono la sequenza nel nome.
    """

    # Elenco di tutti gli elementi nella cartella
    elementi = os.listdir(percorso)

    for elemento in elementi:
        percorso_completo = os.path.join(percorso, elemento)

        # Controllo che sia un file e non una directory
        if os.path.isfile(percorso_completo):

            # Se la sequenza è contenuta nel nome del file allora elimino
            if sequenza in elemento:
                os.remove(percorso_completo)
                print(f"Eliminato: {elemento}")

percorso_input = input("Inserisci il percorso da analizzare: ")
sequenza_input = input("Inserisci la sequenza da cercare nei nomi dei file: ")

eliminaFiles(percorso_input, sequenza_input)
