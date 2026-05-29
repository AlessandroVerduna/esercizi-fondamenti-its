"""
    Autore: Alessandro Verduna
    Data: 29/05/2026

    Consegna: Quinto Esercizio
        Creare una classe AritmeticaDue con attributi operando1 e operando2. Definire il
        costruttore utilizzando parametri con valori predefiniti e il metodo str.
        Aggiungere due metodi uno che restituisca la differenza e l'altro il prodotto dei due
        operandi. Implementare un terzo metodo che permetta il confronto tra il risultato del
        prodotto di due oggetti AritmeticaDue (in sostanza indicare se il prodotto è maggiore di
        quello calcolato nell'oggetto AritmeticaDue passato come parametro).

        Derivare dalla classe AritmeticaDue la classe AritmeticaTre aggiungendo l'attributo
        operando3. Ridefinire il costruttore, il metodo str e i tre metodi differenza, prodotto e
        confronto. Aggiungere un metodo per il calcolo della somma di tutti gli attributi.
        Provare le classi e i metodi implementati.
"""

class AritmeticaDue(object):
    def __init__(self, operando1, operando2):
        self.__operando1 = operando1
        self.__operando2 = operando2

    def __str__(self):
        return f"Operando 1: {self.__operando1}, operando 2: {self.__operando2}"

    def differenza(self):
        return self.__operando1 - self.__operando2
    
    def prodotto(self):
        return self.__operando1 * self.__operando2
    
    def confronto(self, val: object):
        if self.prodotto() > val.prodotto():
            return True
        else:
            return False
        
class AritmeticaTre(AritmeticaDue):
    def __init__(self, operando1, operando2, operando3):
        super().__init__(operando1, operando2)
        self.__operando3 = operando3

    def __str__(self):
        return f"{super().__str__()}, operando 3: {self.__operando3}"
    
    def differenza(self):
        return super().differenza() - self.__operando3

    def prodotto(self):
        return super().prodotto() * self.__operando3
    
    def confronto(self, val: object):
        if self.prodotto() > val.prodotto():
            return True
        else:
            return False
        
    def somma(self):
        return self.__operando1 + self.__operando2 + self.__operando3
    
numeri1 = AritmeticaDue(10,8)
numeri2 = AritmeticaDue(10,50)

numeri3 = AritmeticaTre(10,5,2)
numeri4 = AritmeticaTre(1,111,4)

print(numeri1.differenza())
print(numeri1.prodotto())
print(numeri1.confronto(numeri2))

print(numeri3.confronto(numeri4))

print(numeri3.somma())