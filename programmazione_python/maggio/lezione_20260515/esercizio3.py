"""
Autore: Alessandro Verduna
Data: 15/05/2026

Consegna: Terzo Esercizio
    Scrivete un programma Python per ottenere il valore massimo e minimo in un dizionario.
"""

def logica(dizionario_local: dict):
    """
    Estrae il valore minimo e il valore massimo presenti in un dizionario.

    Parametri:
        dizionario_local (dict): dizionario contenente coppie chiave-valore numeriche.

    Ritorna:
        minimo (int/float): il valore più basso presente nel dizionario.
        massimo (int/float): il valore più alto presente nel dizionario.
    """
    lista_valori = []

    for numero in dizionario_local.values():
        lista_valori.append(numero)

    minimo = min(lista_valori)
    massimo = max(lista_valori)

    return minimo, massimo


def main():
    """
    Funzione principale del programma.

    Definisce un dizionario di esempio,
    richiama la funzione logica() per ottenere minimo e massimo,
    e stampa i risultati.
    """
    dizionario = {"a": 5, "b": 8, "c": 11, "d": 99, "e": 0}

    minimo, massimo = logica(dizionario)

    print(f"Il valore più basso è: {minimo} mentre il valore massimo è: {massimo}")


if __name__ == "__main__":
    main()
