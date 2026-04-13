"""
    Autore: Alessandro Verduna
    Data: 13/04/2026
    
    Consegna: Terzo esercizio
        Scrivi un programma per trovare il secondo numero più piccolo in una lista.
"""

def logica(lista_local):
    lista_local_ordinata = sorted(lista_local)
    risultato_local = lista_local_ordinata[1]
    return risultato_local

def main():
    lista = [10,9,2,3,4,5]
    risultato = logica(lista)
    print(f"Il secondo numero più piccolo della lista {lista} è: {risultato}")
    
if __name__ == '__main__':
    main()