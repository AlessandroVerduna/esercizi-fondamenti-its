"""
    Autore: Alessandro Verduna
    Data: 06/03/2026

    Titolo: Secondo esercizio (prima parte)
        Scrivere un programma che legga i coefficienti a, b e c di un'equazione di secondo grado
        ax2+bx+c=0 e ne scriva le soluzioni.

"""
import math

print("Data un espressione AX^2 + BX + C")

verifica = False

while verifica == False:
    try: 
        a, b, c = map(float,input("Inserisci un valore per A, uno per B e uno per C separati da uno spazio e ti dirò il valore di X: ").split())

    except:
            print("Inserisci solo numeri. Altri caratteri non sono ammessi!")
    else:
        verifica = True    
        
        try:
            x1 = ((-1 * b) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            x2 = ((-1 * b) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        
        except:
            print("L'equazione non ha soluzioni reali")
            print("Problema risolto!")

        else:
            if x1 == x2:
                print(f"C'è solo un possibile valore di X ed è: {round(x1,2)}")
            else:
                print(f"X può avere du valori e sono: {round(x1,2)} e {round(x2,2)}")
        
            print("Problema risolto!")