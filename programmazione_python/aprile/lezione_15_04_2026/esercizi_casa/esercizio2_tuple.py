"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Secondo esercizio
        Scrivere un programma per invertire una tupla
        Esempio:
        tpleIN=('a', 'c', 'f')
        pleOUT=('f', 'c', 'a')
"""

def logica(tupla_in_local):
    """
    Inverte l'ordine degli elementi di una tupla.

    Parametri:
        tupla_in_local (tuple): tupla da invertire.

    Ritorna:
        tuple: nuova tupla con gli elementi in ordine inverso.

    Logica:
        Utilizza lo slicing con passo -1 ([::-1]) per creare una copia della tupla con ordine invertito.
    """
    tupla_processata_local = tupla_in_local[::-1]
    return tupla_processata_local

def controllo_tupla_annidata(tupla_local):
    """
    Controlla se la tupla contiene altre tuple al suo interno.

    Parametri:
        tupla_local (tuple): tupla da analizzare.

    Ritorna:
        str: messaggio informativo sul tipo di tupla.

    Note:
        Se viene trovata una tupla annidata, il programma segnala che NON verrà effettuato un deep reverse.
        Se non ci sono tuple annidate, procede normalmente.
    """
    for elemento in tupla_local:
        if isinstance(elemento, tuple):
            return "Questa è una tupla annidata, non verrà affto un DEEP REVERSE!"
    else:
        return "Sto processando..."

def main():
    """
    Funzione principale del programma.
    - Definisce una tupla di input.
    - Controlla se contiene tuple annidate.
    - Inverte la tupla tramite la funzione logica().
    - Stampa il risultato finale.
    """
    tupla_in = ('a', 'b', 'c') 
    messaggio = controllo_tupla_annidata(tupla_in)
    tupla_processata = logica(tupla_in)
    print(messaggio)
    print(f"La tupla di partenza era {tupla_in}. La tupla finale è {tupla_processata}")
    
if __name__ == "__main__":
    main()