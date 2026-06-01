"""
Autore: Alessandro Verduna
Data: 29/05/2026

Consegna: Quinto Esercizio
    Creare una classe AritmeticaDue con attributi operando1 e operando2. Definire il
    costruttore utilizzando parametri con valori predefiniti e il metodo str.
    Aggiungere due metodi: uno che restituisca la differenza e l'altro il prodotto dei due
    operandi. Implementare un terzo metodo che permetta il confronto tra il risultato del
    prodotto di due oggetti AritmeticaDue.

    Derivare dalla classe AritmeticaDue la classe AritmeticaTre aggiungendo l'attributo
    operando3. Ridefinire costruttore, metodo str, differenza, prodotto e confronto.
    Aggiungere un metodo per il calcolo della somma di tutti gli attributi.
    Provare le classi e i metodi implementati.
"""

class AritmeticaDue(object):
    """
    Classe che rappresenta operazioni aritmetiche con due operandi.
    Gli attributi sono privati e accessibili tramite property.
    """

    def __init__(self, operando1=0, operando2=0):
        """
        Costruttore con parametri predefiniti.

        Parametri:
            operando1 (int/float): primo operando.
            operando2 (int/float): secondo operando.
        """
        self.__operando1 = operando1
        self.__operando2 = operando2

    def __str__(self):
        """Restituisce una rappresentazione leggibile dell'oggetto."""
        return f"Operando 1: {self.__operando1}, operando 2: {self.__operando2}"

    # Property per accedere agli attributi privati
    @property
    def operando1(self):
        return self.__operando1

    @property
    def operando2(self):
        return self.__operando2

    def differenza(self):
        """Restituisce la differenza tra i due operandi."""
        return self.__operando1 - self.__operando2

    def prodotto(self):
        """Restituisce il prodotto dei due operandi."""
        return self.__operando1 * self.__operando2

    def confronto(self, val):
        """
        Confronta il prodotto dell'oggetto chiamante con quello dell'oggetto passato.

        Parametri:
            val (AritmeticaDue): oggetto da confrontare.

        Ritorna:
            bool: True se il prodotto dell'oggetto chiamante è maggiore.
        """
        return self.prodotto() > val.prodotto()


class AritmeticaTre(AritmeticaDue):
    """
    Classe derivata che aggiunge un terzo operando e ridefinisce i metodi.
    """

    def __init__(self, operando1=0, operando2=0, operando3=0):
        """
        Costruttore ridefinito con tre operandi.
        """
        super().__init__(operando1, operando2)
        self.__operando3 = operando3

    def __str__(self):
        """Restituisce una rappresentazione leggibile dell'oggetto."""
        return f"{super().__str__()}, operando 3: {self.__operando3}"

    def differenza(self):
        """Restituisce la differenza tra i tre operandi."""
        return super().differenza() - self.__operando3

    def prodotto(self):
        """Restituisce il prodotto dei tre operandi."""
        return super().prodotto() * self.__operando3

    def confronto(self, val):
        """Confronta il prodotto dell'oggetto chiamante con quello dell'altro oggetto."""
        return self.prodotto() > val.prodotto()

    def somma(self):
        """Restituisce la somma dei tre operandi."""
        return self.operando1 + self.operando2 + self.__operando3


# Test delle classi come richiesto dalla consegna
numeri1 = AritmeticaDue(10, 8)
numeri2 = AritmeticaDue(10, 50)

numeri3 = AritmeticaTre(10, 5, 2)
numeri4 = AritmeticaTre(1, 111, 4)

print(numeri1.differenza())
print(numeri1.prodotto())
print(numeri1.confronto(numeri2))

print(numeri3.confronto(numeri4))

print(numeri3.somma())
