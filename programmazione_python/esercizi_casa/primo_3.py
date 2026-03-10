"""
    Autore: Alessandro Verduna
    Data: 07/03/2026

    Titolo: Terzo esercizio (prima parte)
        Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la
        lunghezza
"""

verificatore = False

while verificatore == False:
    try:
        # Richiesta in INPUT del valore del raggio e verifica che il valore si accettabile (es. maggiore di ZERO e NO lettere)
        raggio = float(input("Inserisci il valore del raggio di un cerchio e ti calcolerò il perimetro e l'area: "))
        if raggio <= 0:
            print("Il raggio non può essere 0 o negativo")
        else:
            print("Raggio valido. Calcolo\n...\n...\n...")
            verificatore = True
    except:
        print("Non puoi inserire valori che non siano numeri!")

# Esecuzione della logica matematica
area = 3.14 * (raggio ** 2)
perimetro = raggio * 2 * 3.14

# Viene stampata nel terminale la soluzione
print(f"L'area è {round(area,2)} e la circonferenza è {round(perimetro,2)}")