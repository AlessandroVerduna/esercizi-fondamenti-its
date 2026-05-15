"""
    Autore: Alessandro Verduna
    Data: 15/05/2025
    
    Consegna: Secondo Esercizio
        Scrivete uno script Python per generare e stampare un dizionario che contenga un numero
        (compreso tra 1 e n) nella forma (x, x*x).
        
        Esempio:
        n = 5
        Dizionario: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def logica(n_locale):
    dizionario_locale = {}
    for i in range(1, n_locale + 1):
        dizionario_locale[i] = i ** 2
    return dizionario_locale

def main():
    n = 5
    
    dizionario_finale = logica(n)
    
    print(dizionario_finale)
    
if __name__ == "__main__":
    main()