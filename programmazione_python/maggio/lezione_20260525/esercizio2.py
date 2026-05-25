"""
Autore: Alessandro Verduna
Data: 25/05/2026

Consegna: Secondo Esercizio
    Creare una classe Rettangolo con attributi base e altezza.
    Costruire tutti i metodi setter e getter per gli attributi.
    Aggiungere i metodi per il calcolo dell'area e del perimetro.
    Implementare un metodo di nome “contiene” che ha come parametro un oggetto rettangolo.
    Tale metodo deve restituire True se il rettangolo oggetto chiamante contiene il rettangolo
    oggetto parametro, False altrimenti.
    Un rettangolo “contiene” un altro quando la sua altezza e la sua base sono maggiori
    rispettivamente della base e dell'altezza del secondo rettangolo.
"""

class Rettangolo(object):
    """
    Classe che rappresenta un rettangolo tramite base e altezza.
    Entrambi gli attributi sono privati e gestiti tramite property.
    """

    def __init__(self, base, altezza):
        """
        Inizializza un nuovo rettangolo.

        Parametri:
            base (float/int): lunghezza della base.
            altezza (float/int): lunghezza dell'altezza.
        """
        self.__base = base
        self.__altezza = altezza

    # Getter
    @property
    def base(self):
        """Restituisce la base del rettangolo."""
        return self.__base

    @property
    def altezza(self):
        """Restituisce l'altezza del rettangolo."""
        return self.__altezza

    # Setter
    @base.setter
    def base(self, val):
        """Imposta un nuovo valore per la base."""
        self.__base = val

    @altezza.setter
    def altezza(self, val):
        """Imposta un nuovo valore per l'altezza."""
        self.__altezza = val

    # Metodi funzionali
    def calcolaArea(self):
        """Calcola e restituisce l'area del rettangolo."""
        return self.__base * self.__altezza

    def calcolaPerimetro(self):
        """Calcola e restituisce il perimetro del rettangolo."""
        return 2 * (self.__base + self.__altezza)

    def contiene(self, altro_rettangolo):
        """
        Verifica se il rettangolo chiamante contiene un altro rettangolo.

        Parametri:
            altro_rettangolo (Rettangolo): rettangolo da confrontare.

        Ritorna:
            bool: True se il rettangolo chiamante contiene quello passato come parametro.
        """
        return (
            self.__base > altro_rettangolo.base and
            self.__altezza > altro_rettangolo.altezza
        )


# Test della classe come richiesto dalla consegna
rettangolo1 = Rettangolo(10, 5)
rettangolo2 = Rettangolo(1, 20)

print(rettangolo1.contiene(rettangolo2))
print(rettangolo1.calcolaArea())
print(rettangolo2.calcolaPerimetro())
