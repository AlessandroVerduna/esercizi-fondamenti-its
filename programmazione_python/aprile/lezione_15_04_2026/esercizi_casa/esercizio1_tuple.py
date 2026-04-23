"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Primo esercizio
        Scrivere un programma per rimuovere l'n- esimo elemento da una tupla non vuota.
"""

def logica(tupla_local, posizione):
    """
    Rimuove l'elemento in posizione 'posizione' dalla tupla fornita.

    Parametri:
        tupla_local (tuple): tupla di partenza, non vuota.
        posizione (int): indice dell'elemento da rimuovere (0-based).

    Ritorna:
        tuple: nuova tupla senza l'elemento in posizione indicata.

    Logica:
        Si divide la tupla in due parti e si concatenano le due parti per ottenere la tupla finale.
    """
    tupla1, tupla2 = tupla_local[:posizione], tupla_local[posizione+1:]
    tupla_processata_local = tupla1 + tupla2
    return tupla_processata_local

def controllo(tupla_local, posizione):
    """
    Controlla che la posizione inserita sia valida per la tupla.

    Parametri:
        tupla_local (tuple): tupla su cui effettuare il controllo.
        posizione (int): indice da verificare.

    Ritorna:
        bool: True se la posizione è valida, False altrimenti.

    Una posizione è valida se:
        Non è negativa e non è minore della lunghezza della tupla.
    """
    if (posizione + 1) > len(tupla_local) or posizione < 0:
        return False
    else:
        return True

def main():
    """
    Funzione principale del programma.
    Richiede all'utente la posizione dell'elemento da rimuovere,
    verifica la validità dell'indice tramite controllo(),
    ed esegue la rimozione tramite logica().
    """
    tupla = (1, 2, 3, 4, 5, 6)
    posizione = int(input("Inserisci la posizione dell'elemento da rimuovere (NO posizioni negative): "))
    if controllo(tupla, posizione):
        tupla_processata = logica(tupla, posizione)
        print(f"La tupla processata è: {tupla_processata}")
    else:
        print("Inserita una posizione non valida")
    
if __name__ == "__main__":
    main()