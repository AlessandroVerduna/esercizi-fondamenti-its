"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Quarto Esercizio
        Scrivere un programma per contare gli elementi in una lista finché non si incontra un
        elemento di tipo tupla. [Suggerimento: si usi la funzione isinstance( ) ]
"""

def logica(lista_input_locale):
    """
    Conta quanti elementi sono presenti nella lista prima di incontrare
    il primo elemento di tipo tupla.

    Parametri:
        lista_input_locale (list): lista contenente elementi di qualsiasi tipo.

    Ritorna:
        int: numero di elementi letti prima di incontrare una tupla.
             Se non viene trovata alcuna tupla, restituisce la lunghezza totale della lista.
    """
    contatore = 0
    for elemento in lista_input_locale:
        if isinstance(elemento, tuple):
            return contatore
        else:
            contatore += 1
    return contatore
    
def main():
    """
    Funzione principale del programma.
    - Definisce una lista di input.
    - Richiama la funzione logica() per contare gli elementi prima di una tupla.
    - Stampa un messaggio diverso a seconda che la lista contenga o meno tuple.
    """
    lista_input = ['ciao', 41, 4.3, True, 'fine', 41]
    numero_elementi = logica(lista_input)
    if len(lista_input) == numero_elementi:
        print("La lista non ha tuple")
    else:
        print(f"Prima di incontrare una tupla nella lista ci sono: {numero_elementi} elementi")
    
if __name__ == "__main__":
    main()