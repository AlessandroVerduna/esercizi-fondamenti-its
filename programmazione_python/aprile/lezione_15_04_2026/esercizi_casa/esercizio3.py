"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Terzo Esercizio
        Scrivere un programma per sostituire l'ultimo valore delle liste in una tupla con un valore
        richiesto in input.
        Esempio:
        valore : 100
        TuplaIN: ([10, 20, 40], [40, 50, 60], [70, 80, 90])
        TuplaOUT: ([10, 20, 100], [40, 50, 100], [70, 80, 100])
"""

def logica(tupla_in_locale, valore_locale):
    """
    Sostituisce l'ultimo elemento di ogni lista contenuta nella tupla.

    Parametri:
        tupla_in_locale (tuple): tupla contenente liste non vuote.
        valore_locale (int): valore da inserire come ultimo elemento di ogni lista.

    Ritorna:
        tuple: la tupla originale, le cui liste interne sono state modificate in place.
    """
    for elemento in tupla_in_locale:
        elemento[-1] = valore_locale
    return tupla_in_locale

def controllo_liste(tupla_local):
    """
    Verifica che tutti gli elementi della tupla siano liste NON vuote.

    Parametri:
        tupla_local (tuple): tupla da controllare.

    Ritorna:
        bool: True se tutti gli elementi sono liste e non sono vuote, False altrimenti.
    """
    for elemento in tupla_local:
        if not isinstance(elemento, list) or len(elemento) == 0:
            return False
    return True

def main():
    """
    Funzione principale del programma.
    - Definisce una tupla contenente liste.
    - Richiede all'utente un valore intero da inserire come ultimo elemento delle liste.
    - Verifica la validità della tupla tramite controllo_liste().
    - Se valida, applica la sostituzione tramite logica().
    - Stampa il risultato finale.
    """
    tupla_in = ([10, 20, 40], [], [70, 80, 90])
    valore = int(input("Inserisci un valore che inserirò come ultimo nelle liste contenuto nella tupla: "))
    if controllo_liste(tupla_in):
        tupla_processata = logica(tupla_in, valore)
        print(f"Questa era la tupla iniziale: {tupla_in} mentre questa è la tupla processata: {tupla_processata}")
    else:
        print("La tupla fornita non conteneva solo liste o una delle liste inserita è vuota")
    
if __name__ == "__main__":
    main()