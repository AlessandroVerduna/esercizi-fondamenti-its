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
    for elemento in tupla_in_locale:
        elemento[-1] = valore_locale
    return tupla_in_locale

def main():
    tupla_in = ([10, 20, 40], [40, 50, 60], [70, 80, 90])
    valore = int(input("Inserisci un valore che inserirò come ultimo nelle liste contenuto nella tupla: "))
    tupla_processata = logica(tupla_in, valore)
    print(f"Questa era la tupla iniziale: {tupla_in} mentre questa è la tupla processata: {tupla_processata}")
    
if __name__ == "__main__":
    main()