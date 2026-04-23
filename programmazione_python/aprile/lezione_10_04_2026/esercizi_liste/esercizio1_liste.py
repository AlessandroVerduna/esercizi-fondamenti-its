"""
    Autore: Alessandro Verduna
    Data: 10/04/2026

    Consegna: Primo Esercizio
        Scrivere un programma python che rimuova gli elementi duplicati da una lista.
        Esempio:
        listaIN = [2, -4 ,5,6,5,5,2]
        listaOUT = [2,-4,5,6]
"""

def logica(listaIN_locale):
    """
    Rimuove i duplicati dalla lista mantenendo l'ordine originale.
    
    Scorre la lista in ingresso e aggiunge ogni elemento solo se
    non è già presente nella lista di output.
    """
    listaOUT_locale = []
    for elemento in listaIN_locale:
        if elemento in listaOUT_locale:
            continue
        else:
            listaOUT_locale += [elemento]
    return listaOUT_locale
    


def main():
    """
    Funzione principale del programma.

    Definisce due liste predefinite, richiama la funzione logica()
    per verificare se hanno elementi in comune e stampa il risultato.
    """
    listaOUT = []
    listaIN = [2,-4,5,6,5,5,2, 2, 2, 55]
    listaOUT = logica(listaIN)
    print(listaOUT)

if __name__ == '__main__':
    main()
