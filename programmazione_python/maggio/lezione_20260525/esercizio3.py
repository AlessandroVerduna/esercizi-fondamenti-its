"""
Autore: Alessandro Verduna
Data: 25/05/2026

Consegna: Terzo Esercizio
    1 - Creare una classe Calcolo con un costruttore di default (senza parametri) che consenta
        di eseguire vari calcoli su numeri interi.
    2 - Creare un metodo chiamato Factorial() che permetta di calcolare il fattoriale di un
        intero. Testare il metodo istanziando la classe.
    3 - Creare un metodo chiamato Sum() che consenta di calcolare la somma dei primi n
        interi 1 + 2 + 3 + .. + n. Prova questo metodo.
    4 - Creare un metodo tableMult() che crea e visualizza la tabellina di un dato intero.
        Quindi creare un metodo allTablesMult() per visualizzare tutte le tabelline dei numeri
        interi 1, 2, 3, ..., 9.
"""

class Calcolo(object):
    """
    Classe che permette di eseguire vari calcoli matematici su numeri interi.
    Il costruttore è di default e non richiede parametri.
    """

    def __init__(self):
        """Costruttore di default (vuoto)."""
        pass

    def Factorial(self, val):
        """
        Calcola il fattoriale di un numero intero.

        Parametri:
            val (int): numero intero di cui calcolare il fattoriale.

        Ritorna:
            risultato (int): fattoriale del numero.
        """
        risultato = 1
        for i in range(1, val + 1):
            risultato *= i
        return risultato

    def Sum(self, val):
        """
        Calcola la somma dei primi n numeri interi.

        Parametri:
            val (int): numero fino al quale sommare.

        Ritorna:
            risultato (int): somma 1 + 2 + ... + val.
        """
        risultato = 0
        for i in range(0, val + 1):
            risultato += i
        return risultato

    def tableMult(self, val):
        """
        Genera la tabellina di un numero intero.

        Parametri:
            val (int): numero di cui generare la tabellina.

        Ritorna:
            risultato (list): lista contenente i primi 10 multipli del numero.
        """
        risultato = []
        for i in range(1, 11):
            risultato.append(val * i)
        return risultato

    def allTablesMult(self):
        """
        Genera tutte le tabelline dei numeri da 1 a 9.

        Ritorna:
            risultato (list): lista di liste, ciascuna contenente la tabellina di un numero.
        """
        risultato = []
        for i in range(1, 10):
            risultato.append(self.tableMult(i))
        return risultato


# Test della classe come richiesto dalla consegna
calc = Calcolo()

print(calc.Factorial(5))
print(calc.Sum(5))
print(calc.tableMult(5))
print(calc.allTablesMult())
