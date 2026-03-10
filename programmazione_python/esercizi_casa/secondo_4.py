""" 
    Autore: Alessandro Verduna
    Data: 08/03/2026

    Titolo: Quarto esercizio (seconda parte)
        Scrivere un programma che legge N numeri da tastiera, N dato in input, e ne restituisca il minimo. 
"""
# Questa funzione chiede all'utente quanto lunga deve eessere la lista di numeri e verifica che vengano inseriti input accettati
# Restituisce il numero usato come riferimento per la lunghezza della lista
def quanti_numeri():
    while True:
        try:
            lunghezza = int(input("Quanti numeri nella serie? "))
            if lunghezza <= 0:
                print("Inserirre SOLO numeri INTERI POSITIVI e MAGGIORI DI ZERO")
                continue
            else:
                return lunghezza
        except ValueError:
            print("Inserirre SOLO numeri INTERI POSITIVI e MAGGIORI DI ZERO. Non si possono inserire altri caratteri")

# Questa funzione prende il numero per la lunghezza della lista inserito precedentemente e 
# domanda di volta in volta un numero accettando solo alcuni input (es. NO lettere)
# Restituisce una lista di numeri
def inserimento_numeri(cicli):
    lista = []
    for i in range(cicli):
        try:
            lista.append(float(input("Inserisci un numero ")))
        except:
            print("Questo valore non sarà inserito nella lista in qaunto invalido")
    return lista
    
# Questa è la funzione MAIN in cui vengono concatenate le funzioni precedenti
# Viene accertato che la lunghezza della lista non sia zero in quanto non si potrebbe trovare il minimo
# Se la lista contiene dei numeri esegue la funzione MIN() che cerca in automatico il numero minore 
def main():
    cicli = quanti_numeri()
    lista = inserimento_numeri(cicli)
    if len(lista) == 0:
        print("Non hai inserito numeri validi. Impossibile individuare il minore")
    else:
        print(f"Il numero più piccolo nella serie è: {min(lista)}")

# Esecuzione della funzione MAIN() che a cascata esegue le altre
if __name__ == "__main__":
    main()