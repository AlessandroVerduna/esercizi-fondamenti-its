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
    tupla_processata_local = tuple(sorted(tupla_in_local, reverse=True))
    return tupla_processata_local

def main():
    tupla_in = ('a', 'c', 'f')
    tupla_processata = logica(tupla_in)
    print(f"La tupla di partenza era {tupla_in} mentre la tupla finale è {tupla_processata}")
    
if __name__ == "__main__":
    main()