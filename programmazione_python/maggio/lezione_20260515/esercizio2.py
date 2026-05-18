"""
Autore: Alessandro Verduna
Data: 15/05/2025

Consegna: Secondo Esercizio
    Scrivete uno script Python per generare e stampare un dizionario che contenga un numero
    (compreso tra 1 e n) nella forma (x, x*x).

    Esempio:
        n = 5
        Dizionario: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def logica(n_locale):
    """
    Genera un dizionario in cui ogni numero da 1 a n è associato al suo quadrato.

    Parametri:
        n_locale (int): il numero massimo fino al quale generare le coppie (x, x*x).

    Ritorna:
        dizionario_locale (dict): dizionario contenente le coppie numero-quadrato.
    """
    dizionario_locale = {}

    for i in range(1, n_locale + 1):
        dizionario_locale[i] = i ** 2

    return dizionario_locale


def main():
    """
    Funzione principale del programma.

    Definisce un valore n,
    richiama la funzione logica() per generare il dizionario,
    e stampa il risultato finale.
    """
    n = 5

    dizionario_finale = logica(n)

    print(dizionario_finale)


if __name__ == "__main__":
    main()
