"""
Autore: Alessandro Verduna
Data: 15/05/2026

Consegna: Primo esercizio
    Progettare una funzione che accetti un numero indefinito di dizionari e restituisca un
    dizionario che è la concatenazione di tutti i dizionari indicati come parametro formale alla
    funzione. Scrivete uno script che utilizzi tale funzione.

    Esempio:
        diz1 = {'v1':1,'v2':2,'v3':3}
        diz2 = {'v4':4,'v5':5,'v6':6}
        diz3 = {'v7':7,'v8':8}

        Dizionario restituito:
        {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4,
         'v5': 5, 'v6': 6, 'v7': 7, 'v8': 8}
"""

def logica(*diz_local: dict) -> dict:
    """
    Unisce un numero indefinito di dizionari in un unico dizionario finale.

    Parametri:
        *diz_local (dict): uno o più dizionari da concatenare.

    Ritorna:
        diz_finale_locale (dict): dizionario risultante dalla concatenazione
        di tutti i dizionari passati come argomento.
    """
    diz_finale_locale = {}

    for dizionario in diz_local:
        diz_finale_locale.update(dizionario)

    return diz_finale_locale


def main():
    """
    Funzione principale del programma.

    Definisce alcuni dizionari di esempio,
    richiama la funzione logica() per concatenarli
    e stampa il dizionario risultante.
    """
    diz1 = {'v1': 1, 'v2': 2, 'v3': 3}
    diz2 = {'v4': 4, 'v5': 5, 'v6': 6}
    diz3 = {'v7': 7, 'v8': 8}
    diz4 = {'v9': 9, 'v10': 10}

    diz_finale = logica(diz1, diz2, diz3, diz4)

    print(diz_finale)
    print(type(diz_finale))


if __name__ == "__main__":
    main()
