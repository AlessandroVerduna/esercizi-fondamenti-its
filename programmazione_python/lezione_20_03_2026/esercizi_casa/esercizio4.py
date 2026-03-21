"""
    Autore: Alessandro Verduna
    Data: 21/03/2026

    Consegna: La seguente è la formula per valutare numericamente il numero di Nepero (vedi PDF).  
        4.a Scrivere una funzione che restituisca un valore approssimato di e all'ennesimo termine, dove N è inserito 
        come parametro formale alla funzione.  Esempio: calcola_e(3) restituirà il valore di e calcolato con tre termini 
        della (1), cioè: e= 1/0! + 1/1! + 1/2! = 1 + 1 + 0.5 = 2.5 La funzione calcola_e deve richiamare la funzione di 
        calcolo del fattoriale. Scrivere il codice della funzione e il programma principale che la chiama chiedendo in input 
        il numero N.


        4.b Supponendo di porre il numero di Nepero = 2.718281828459045 dico che  errore = calcola_e(N) - Nepero  
        sia l'errore che commetto nella valutazione di e. Modificare la funzione che restituisce la valutazione di e con 
        N termini andando a far restituire anche l'errore commesso nella valutazione.  
        Suggerimento: la funzione calcola_e(N) dovrà restituire due valori,  2.718281828459045 potrebbe essere memorizzato 
        in una variabile globale. esempio: valuta_e(3) restituisce il valore calcolato nel punto 4.a 2.5 e 0,218281828459045 che 
        rappresenta la differenza tra 2.718281828459045 e 2.5 
"""

def fattoriale(n):
    """
    Calcola il fattoriale di un numero intero 'n' fornito in input dall'utente.
    Parametri:
        n (int): numero intero >= 0
    Ritorna:
        int: il valore di n!
    """
    risultato = 1
    for i in range(1, n + 1):
        risultato *= i
    return risultato

def calcola_e(n):
    """
    Calcola un'approssimazione del numero di Nepero usando i primi 'n' termini
    della serie. Calcola anche l'errore rispetto al valore reale di e.
    Parametri:
        n (int): numero di termini della serie da sommare
    Ritorna:
        risultato (float): approssimazione di e
        errore (float): differenza tra risultato e numero di Nepero
    """
    risultato = 0
    global nepero_number
    for i in range(n):
        risultato += 1 / fattoriale(i)
    errore = nepero_number - risultato
    return risultato, errore

def main():
    """
    Funzione principale del programma.
    Chiede all'utente il valore di n.
    Dopodiché chiama la funzione calcola_e(n), notare che 'n' indicato dall'utente viene utilizzato come parametro della funzione.
    """
    correttezza_n = False
    while correttezza_n != True:
        n = input("Definisci N: ")
        if n < 0:
            print("Inserire un valore valido per N!")
        else:
            risultato, errore = calcola_e(n)
            print(f"Il risultato è: {risultato} mentre l'errore è di: {errore}")
            correttezza_n = True

if __name__ == "__main__":
    nepero_number = 2.718281828459045
    main()