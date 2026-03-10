"""
    Autore: Alessandro Verduna
    Data: 07/03/2026

    Titolo: Primo esercizio (seconda parte)
        Si hanno in input due numeri reali A e B e una successione di numeri reali positivi che
        termina con il valore 0. Si vuole in output la media dei soli numeri compresi tra A e B.
        Esempio:
        INPUT: A=2 B= 3.5 Successione: -3.4 4 2.5 3 10 0
        OUTPUT: 2.75 [ perchè media=(2.5+3)/2=2.75]
"""
# Dichiarazione delle variabili utilizzate successivamente
lista = []
verificatore = False
verificatore2 = False
lista_media = 0
contatore = 0
media = 0
c = 0

# Inserimento di A e B e verifica che siano effettivamente due numeri (es. non due lettere)
while verificatore == False:
    try:
        a,b = map(float,input("Inserisci qui due numeri che definiremo A e B separati da uno spazio: ").split())
        verificatore = True
    except:
        print("Vengono accettati solo numeri come valori. I caratteri non sono accettati!")    
    
# Inserimento uno alla volta dei numeri della successione che termina nel momento in cui il numero inserito è ZERO
# Verifica che non siano inserite lettere
while verificatore2 == False:    
    try:
        successione = float(input("Inserisci ora un numero che verrà aggiunto alla successione (per terminare inserire 0): "))

        if successione != 0:
            lista.append(successione)
        else:
            verificatore2 = True
    except:
        print("Vengono accettati solo numeri come valori. I caratteri non sono accettati!")

# Riordino di A e B di modo che A sia sempre il numero più piccolo tra i due
if a > b:
    c = b
    b = a
    a = c

# Vengono presi in cosniderazione solo i numeri che rientrano nel range A e B  e calcolo della MEDIA
# Se non ci sono numeri che soddisfano questa condizione l'impossibilità di calcolare viene esplicitata attraverso un messaggio
for i in lista:
    if i > a and i < b:
        lista_media += i
        contatore += 1

if contatore == 0:
    print("Non avendo inserito numeri la media non è calcolabile")
else:
    media = lista_media / contatore

    print(f"La media è: {media}")
