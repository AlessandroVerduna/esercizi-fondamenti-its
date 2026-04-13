"""
    Autore: Alessandro Verduna
    Data: 13/04/2026
    
    Consegna: Secondo Esercizio
        Scrivere un programma che date due liste stampi "OK" se hanno almeno un membro
        comune altrimenti stampi "KO".
        Esempio:
        ● lista1=[1,5,8] lista2=[3,1,10] -> output: "OK"
        ● lista1=[1,5,8] lista2=[3,11,10] -> output: "KO"
"""

def logica(lista1_local, lista2_local):
    """
    Verifica se le due liste hanno almeno un elemento in comune
    e stampa il risultato.
    """
    verificatore = False
    for elemento in lista1_local:
        if elemento in lista2_local:
            verificatore = True
            
    if verificatore == True:
        print("OK")
    else:
        print("KO")


def main():
    """
    Funzione principale del programma.

    Definisce due liste predefinite, richiama la funzione logica()
    per verificare se hanno elementi in comune e stampa il risultato.
    """
    lista1=[1,5,8] 
    lista2=[3,1,10]
    
    logica(lista1, lista2)
    
    
if __name__ == '__main__':
    main()