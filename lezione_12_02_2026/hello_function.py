""" In questo modulo introduciamo le funzioni di Python """

import random as rnd

#print(help(rnd))

#Definizione di funzione. Tecnicamente è una 'procedura' perché non ha un INPUT e non ha un OUTPUT
# La distinzione è semplicemente logica, pYthon non distingue tra le due
def mia_funzione():
    saluti = ["Buongiorno", "Ciao", "Buonasera", "Hello"]
    print(f"{rnd.choice(saluti)}")

def addizione(a: int,b: int = 0): #a e b sono VARIABILI LOCALI che non escono dalla definizione della funzione
    """
    Docstring for addizione
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    """
    return a + b

def sottrazione(a,b = 0): #posso assegnare un valore di default in modo da prevenire il mancato cuminamento da perte dell'utente di un valore
    return a - b

def somma(*numeri):
    totale = 0
    for n in numeri:
        totale = totale + n
    return totale


numero_1 = 88
numero_2 = 24

#Richiamo della funzione
mia_funzione()
#print(addizione(addendo2 = numero_1, addendo1 = numero_2)) #le FUNZIONI POSSONO DIVENATRE ARGOMENTO DI ALTRE FUNZIONI
print(sottrazione(numero_1,numero_2))
print(sottrazione(addizione(9,1),sottrazione(8,3)))
print(numero_1,numero_2)

miao = input("Dammi dei numeri")
print(somma(miao))

# mia_funzione()
# mia_funzione()
# mia_funzione()