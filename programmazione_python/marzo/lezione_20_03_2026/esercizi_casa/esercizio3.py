"""
    Autore: Alessandro Verduna
    Data: 21/03/2026

    Consegna: Terzo esercizio
        Conversione temperatura: implementare una funzione convertiCF che converta una temperatura espressa 
        in gradi Fahrenheit in una temperatura espressa in gradi Celsius. 
        Usare la seguente formula: C = (F   - 32) * 5 / 9 Creare un programma principale che richiami 
        la funzione e ne stampi il risultato visualizzando solo 3 cifre decimali. 
"""

def convertiCF(temperatura_fahrenheit):
    """
    Converte una temperatura da Fahrenheit a Celsius usando la formula standard.
    Parametri:
        temperatura_fahrenheit (float): valore della temperatura in gradi Fahrenheit.
    Ritorna:
        float: temperatura convertita in gradi Celsius.
    """
    temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9
    return temperatura_celsius
    
def main():
    """
    Funzione principale del programma.
    Richiede all'utente una temperatura in Fahrenheit, la converte in Celsius
    tramite la funzione convertiCF e stampa il risultato arrotondato a 3 decimali.
    """

    temperatura_fahrenheit = float(input("Inserisci una temperatura in Fahrenheit e la convertirò in Celsius: "))
    temperatura_celsius = convertiCF(temperatura_fahrenheit)
    print(f"La temperatura convertità in Celsius è {round(temperatura_celsius, 3)}")

if __name__ == "__main__":
    main()