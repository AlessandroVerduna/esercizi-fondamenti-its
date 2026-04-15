"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Quarto Esercizio
        Scrivere un programma per contare gli elementi in una lista finché non si incontra un
        elemento di tipo tupla. [Suggerimento: si usi la funzione isinstance( ) ]
"""

def logica(lista_input_locale):
    contatore = 0
    for elemento in lista_input_locale:
        if isinstance(elemento, tuple):
            return contatore
        else:
            contatore += 1
    return contatore
    
def main():
    lista_input = ['ciao', 41, 4.3, True, 'fine', 41]
    numero_elementi = logica(lista_input)
    if len(lista_input) == numero_elementi:
        print("La lista non ha tuple")
    else:
        print(f"Prima di incontrare una tupla nella lista ci sono: {numero_elementi} elementi")
    
if __name__ == "__main__":
    main()