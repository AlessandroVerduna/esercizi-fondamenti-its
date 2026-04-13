"""
    Autore: Alessandro Verduna
    Data: 13/04/2026
    
    Consegna: Quarto esercizio
        Scrivere un programma Python per dividere una data lista in due parti in cui viene data la
        lunghezza della prima parte della lista.
        Esempio:
        Lista originale: [1, 1, 2, 3, 4, 4, 5, 1]
        Lunghezza della prima parte della lista: 3
        Output : Prima parte: [1, 1, 2] ,
        Seconda parte: [3, 4, 4, 5, 1]
"""

def logica(lista_local, lunghezza_local):
    """
    Divide una lista in due parti utilizzando lo slicing.

    Parametri:
        lista_local (list): la lista originale da dividere.
        lunghezza_local (int): il numero di elementi che devono costituire la prima parte.

    Ritorna:
        prima_lista_local (list): la prima parte della lista, contenente i primi 'lunghezza_local' elementi.
        seconda_lista_local (list): la parte restante della lista dopo la divisione.
    """
    prima_lista_local = lista_local[:lunghezza_local]
    seconda_lista_local = lista_local[lunghezza_local:]
    return prima_lista_local, seconda_lista_local

def main():
    """
    Funzione principale del programma.

    Definisce una lista predefinita, richiede all'utente il punto di divisione,
    richiama la funzione logica() per dividere la lista e stampa le due liste risultanti.
    """
    lista = [1, 1, 2, 3, 4, 4, 5, 1]
    lunghezza = int(input("Dove vuoi spezzare la lista? "))
    prima_lista_divisa, seconda_lista_divisa = logica(lista, lunghezza)
    print(f"Le nuove liste sono: {prima_lista_divisa} e {seconda_lista_divisa}")

if __name__ == "__main__":
    main()