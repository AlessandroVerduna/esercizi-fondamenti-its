"""
Autore: Alessandro Verduna
Data: 15/05/2026

Consegna: Quarto Esercizio
    Scrivete un programma Python per rimuovere i duplicati dal dizionario.
"""

def logica(dizionario_local):
    """
    Rimuove i valori duplicati da un dizionario mantenendo la prima occorrenza.

    Parametri:
        dizionario_local (dict): dizionario originale da elaborare.

    Ritorna:
        dizionario_output (dict): nuovo dizionario senza valori duplicati.
    """
    dizionario_output = {}

    for chiave, valore in dizionario_local.items():
        if valore not in dizionario_output.values():
            dizionario_output[chiave] = valore

    return dizionario_output


def main():
    """
    Funzione principale del programma.

    Definisce un dizionario con valori duplicati,
    richiama la funzione logica() per rimuoverli
    e stampa il risultato finale.
    """
    dizionario = {'v1': 199, 'v2': 199, 'v3': 3, 'v4': 4, 'v5': 5, 'v6': 6, 'v7': 7, 'v8': 8}
    print(dizionario)

    risultato = logica(dizionario)

    print(risultato)


if __name__ == "__main__":
    main()
