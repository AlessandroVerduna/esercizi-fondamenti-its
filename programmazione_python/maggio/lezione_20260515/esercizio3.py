"""
    Autore: Alessandro Verduna
    Data: 15/05/2026
    
    Consegna: Terzo Esercizio
        Scrivete un programma Python per ottenere il valore massimo e minimo in un dizionario.
"""

def logica(dizionario_local: dict):
    lista_valori = []
    
    for numero in dizionario_local.values():
        lista_valori.append(numero)
        
    minimo = min(lista_valori)
    massimo = max(lista_valori)
    
    return minimo, massimo
    
def main():
    dizionario = {"a": 5, "b": 8, "c": 11, "d": 99, "e": 0}

    minimo, massimo = logica(dizionario)

    print(F"Il valore più basso è: {minimo} mentre il valore massimo è: {massimo}")

if __name__ == "__main__":
    main()