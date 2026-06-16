"""
Autore: Alessandro Verduna
Data: 16/06/2026

Consegna: Secondo Esercizio
    Scrivere un programma che esamini tutte le directories sotto un dato percorso
    e conti tutti i files con una determinata estensione data in input.
    [In prima battuta fermatevi al primo livello di profondità delle directories]
"""

import os

def contaFileEstensione(percorso, estensione):
    """
    Procedura che esamina tutte le directory presenti nel primo livello
    del percorso indicato e conta quanti file hanno l'estensione richiesta.

    Parametri:
        percorso (str): percorso di partenza.
        estensione (str): estensione dei file da contare (senza punto).

    Effetti:
        Stampa a video il numero totale di file trovati.
    """

    # Normalizzo l'estensione (senza punto)
    estensione = estensione.lower().replace(".", "")

    # Elenco degli elementi nel percorso
    elementi = os.listdir(percorso)

    count = 0

    for elemento in elementi:
        percorso_completo = os.path.join(percorso, elemento)

        # Considero solo le directory del primo livello
        if os.path.isdir(percorso_completo):

            # Esamino SOLO il contenuto della directory (non ricorsivo)
            for file in os.listdir(percorso_completo):
                if file.lower().endswith("." + estensione):
                    count += 1

    print(f"Numero di file con estensione '.{estensione}' trovati: {count}")

percorso_input = input("Inserisci il percorso da analizzare: ")
estensione_input = input("Inserisci l'estensione da cercare (es. txt): ")

contaFileEstensione(percorso_input, estensione_input)
