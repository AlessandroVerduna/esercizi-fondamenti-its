"""# dammi un numero causla e da 1 a 100 che ti tieni in memoria mi devi contare quanti 
tenativi impiego per trovare 
il numero e ogni volta mi devi dire se è maggiore o minore e mi dirai indovinato o meno"""

def verifica():
    while True:
        try:
            scelto = int(input("Scegli un numero da uno a cento: "))
            break
        except ValueError:
            print("Inserisci un intero!")

import random as rnd
import time

start = time.time()
casual = rnd.randint(1,100)
counter = 1

while True:
    try:
        scelto = int(input("Scegli un numero da uno a cento: "))
        break
    except ValueError:
        print("Inserisci un intero!")

while scelto != casual:
    if scelto < casual:
        print("Troppo basso")
    else:
        print("Troppo alto")
    counter += 1
    while True:
        try:
            scelto = int(input("Scegli un numero da uno a cento: "))
            break
        except ValueError:
            print("Inserisci un intero!")
print(f"Hai indvoinato e ci hai messo {counter} tentativi")

end = time.time()
elapsed = end - start
print(f"Tempo per l'esecuzione: {elapsed} secondi")