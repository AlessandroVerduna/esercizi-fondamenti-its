"""
    Autore: Alessandro Verduna
    Data: 13/04/2026
    
    Consegna: Terzo esercizio
        Scrivi un programma per trovare il secondo numero più piccolo in una lista.
"""

def logica(lista_local):
    """
    Trova il secondo numero più piccolo all'interno di una lista.

    Parametri:
        lista_local (list): lista di valori numerici da analizzare.

    Ritorna:
        risultato_local (int/float): il secondo valore più piccolo presente nella lista.
                                     Si ottiene ordinando la lista e selezionando l'elemento in posizione 1.
    """
    lista_local_ordinata = sorted(lista_local)
    risultato_local = lista_local_ordinata[1]
    return risultato_local

def main():
    """
    Funzione principale del programma.

    Definisce una lista predefinita, richiama la funzione logica()
    per ottenere il secondo numero più piccolo e stampa il risultato.
    """
    lista = [10,9,2,3,4,5]
    risultato = logica(lista)
    print(f"Il secondo numero più piccolo della lista {lista} è: {risultato}")
    
if __name__ == '__main__':
    main()