"""
    Autore: Alessandro Verduna
    Data: 06/03/2026

    Titolo: Secondo esercizio (prima parte)
        Scrivere un programma che legga i coefficienti a, b e c di un'equazione di secondo grado
        ax2+bx+c=0 e ne scriva le soluzioni.

"""

# Libreria che importa la possibilità di eseguire la funzione math.sqrt() che esegue la radice quadrata dell'argomento in parentesi
# Un'altra possibilità era elevare alla 0.5 (es. x ** 0.5)
import math

print("Data un espressione AX^2 + BX + C")

verifica = False

while verifica == False:
    try: 
        # Verifica che i valori inseriti in input siano accettati (es. no lettere)
        a, b, c = map(float,input("Inserisci un valore per A, uno per B e uno per C separati da uno spazio e ti dirò il valore di X: ").split())
    except:
            print("Inserisci solo numeri. Altri caratteri non sono ammessi!")
    else:
        verifica = True    
        
        try:
            # Esegue le due versione dell'equazione di risoluzione
            x1 = ((-1 * b) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            x2 = ((-1 * b) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        
        except:
            # Nel caso non ci siano soluzioni reali viene stampato un messaggio che esplicita questa condizione ed evita che il programma
            # vada in errore
            print("L'equazione non ha soluzioni reali")
            print("Problema risolto!")

        else:
            # Stampa uno o due valori a seconda delle soluzioni trovate
            if x1 == x2:
                print(f"C'è solo un possibile valore di X ed è: {round(x1,2)}")
            else:
                print(f"X può avere du valori e sono: {round(x1,2)} e {round(x2,2)}")
        
            print("Problema risolto!")