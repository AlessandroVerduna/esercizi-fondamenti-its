"""
    Autore: Alessandro Verduna
    Data: 15/04/2026
    
    Consegna: Primo esercizio
        Scrivere un programma per rimuovere l'n- esimo elemento da una tupla non vuota.
"""

def logica(tupla_local, posizione):
    tupla1, tupla2 = tupla_local[:posizione], tupla_local[posizione+1:]
    tupla_processata_local = tupla1 + tupla2
    return tupla_processata_local

def main():
    tupla = (1, 2, 3, 4, 5, 6)
    posizione = int(input("Inserisci la posizione dell'elemento da rimuovere: "))
    tupla_processata = logica(tupla, posizione)
    print(f"La tupla è: {tupla_processata}")
    
if __name__ == "__main__":
    main()