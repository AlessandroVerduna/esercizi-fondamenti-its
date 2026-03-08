"""
    Autore: Alessandro Verduna
    Data: 06/03/2026

    Titolo: Primo esercizio (prima parte)
        Scrivere un programma che legga i coefficienti a e b di un'equazione di primo grado ax=b e
        ne scriva la soluzione (attenzione al dominio del coefficiente a)

"""

print("Dopo che mi avrai fornito due variabili A e B ti troverò il valore di X nell'equazione: AX = B")

verifica = True
while verifica == True:
    try:
        # Richiesta delle variabili in INPUT
        a,b = map(float,input("Inserisci il valore di A e il valore di B (separati da uno spazio): ").split())
        
        # Esplicitazione, con logica, dei tre possibili casi: risultato calcolabile, indetermianto o impossibile
        if a == 0 and b != 0:
            print("Numeri validi. Calcolo la risposta\n...\n...\n...")
            print("Il valore di X è: impossibile")
        elif a == 0 and b == 0:
            print("Numeri validi. Calcolo la risposta\n...\n...\n...")
            print("Il valore di X è: indeterminato")
        else:
            x = b / a
            print("Numeri validi. Calcolo la risposta\n...\n...\n...")
            print(f"Il valore di X è: {x}")
    except: 
        # Verifivca che siano inseriti valori accettati (es. no lettere)
        print("Inserisci dei numeri ed inseriscine due separati da uno spazio, altri caratteri non sono accettati")
    else:
        # Ferma il ciclo while
        verifica = False