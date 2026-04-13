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
    
    """
    verificatore = False
    for elemento in lista1_local:
        if elemento in lista2_local:
            verificatore = True
            
    if verificatore == True:
        print("C'è un elemento in comune tra le due liste")
    else:
        print("Non c'è un elemento in comune tra le due liste")


def main():
    """
    
    """
    lista1=[1,5,8] 
    lista2=[3,1,10]
    
    logica(lista1, lista2)
    
    
if __name__ == '__main__':
    main()