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

lista = []
verificatore = False
verificatore2 = False
lista_media = 0
contatore = 0
media = 0
c = 0

while verificatore == False:
    try:
        a,b = map(float,input("Inserisci qui due numeri che definiremo A e B separati da uno spazio: ").split())
        verificatore = True
    except:
        print("Vengono accettati solo numeri come valori. I caratteri non sono accettati!")    
    
while verificatore2 == False:    
    try:
        successione = float(input("Inserisci ora un numero che verrà aggiunto alla successione (per terminare inserire 0): "))

        if successione != 0:
            lista.append(successione)
        else:
            verificatore2 = True
    except:
        print("Vengono accettati solo numeri come valori. I caratteri non sono accettati!")

if a > b:
    c = b
    b = a
    a = c

for i in lista:
    if i > a and i < b:
        lista_media += i
        contatore += 1

if contatore == 0:
    print("Non avendo inserito numeri la media non è calcolabile")
else:
    media = lista_media / contatore

    print(f"La media è: {media}")
