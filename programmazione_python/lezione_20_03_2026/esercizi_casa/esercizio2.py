"""
    Autore: Alessandro Verduna
    Data: 20/03/2026
    
    Consegna: Secondo Esercizio
        Creare una funzione che abbia come parametri formali un numero arbitrario di valori numerici. 
        Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli numeri dispari. 
        Successivamente creare un programma che richiami tale funzione e che stampi in output i risultati. 
        No standard input. 
"""

def somma_pari_e_prodotto_dispari(*numeri):
    """
    Esegue la somma per i valori pari mentre esegue la moltiplicazione dei valori dispari.
    Parametri:
        Forniti nel main(), sono hardcoded e sono numeri interi pari e dispari
    Ritorna:
       somma_pari (int): la somma dei numeri pari 
       prodotto_dispari (int): prodotto dei numeri dispari
    """
    somma_pari = 0
    prodotto_dispari = 1
    for numero in numeri:
        if numero % 2 == 0:
            somma_pari += numero
        else:
            prodotto_dispari *= numero
    return somma_pari, prodotto_dispari

def main():
    """
    Funzione principale del programma.
    Dati dei valori predefiniti in input alla funzione somma_pari_e_prodotto_dispari()
    vengono poi stampati i risulati ritornati dalla funzione stessa (somma_pari, prodotto_dispari)
    """
    somma_pari, prodotto_dispari = somma_pari_e_prodotto_dispari(4, 4, 5, 3, 2, 3)
    print(f"La somma dei numeri pari è: {somma_pari} e il prodotto dei numeri dispari è: {prodotto_dispari}")

if __name__ == "__main__":
    main()
