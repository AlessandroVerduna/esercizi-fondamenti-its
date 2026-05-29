"""
    Autore: Alessandro Verduna
    Data: 29/05/2026

    Consegna: Quarto Esercizio
        Si definisca una classe Persona che abbia i seguenti attributi:
        ● nome
        ● indirizzo
        ● età
        Tale classe contiene i seguenti metodi: il costruttore, l'overriding del metodo __str__ e tutti i
        metodi getter e setter degli attributi.
        Si vogliono derivare dalla classe Persona le seguenti classi:
        ● Studente
        ● Lavoratore
        La prima deve avere gli attributi aggiuntivi:
        ● Scuola
        ● Media voti
        La seconda deve avere gli attributi aggiuntivi:
        ● Azienda
        ● Stipendio
        Aggiungere tutti i metodi getter e setter relativi agli attributi aggiuntivi.
        Inoltre effettuare l'overriding dei costruttori e del metodo str inserendo gli attributi
        aggiuntivi.
        Provare le tre classi instanziando almeno un oggetto per classe e provando qualche
        metodo.
"""

class Persona(object):
    def __init__(self, nome, indirizzo, eta):
        self.__nome = nome
        self.__indirizzo = indirizzo
        self.__eta = eta

    def __str__(self):
        return f"Nome: {self.nome}, eta: {self.eta}, indirizzo: {self.indirizzo}"

    @property
    def nome(self):
        return self.__nome
    
    @property
    def indirizzo(self):
        return self.__indirizzo
    
    @property
    def eta(self):
        return self.__eta
    
    @nome.setter
    def nome(self,val):
        self.__nome = val

    @indirizzo.setter
    def indirizzo(self,val):
        self.__indirizzo = val

    @eta.setter
    def eta(self,val):
        self.__eta = val
    
class Studente(Persona):
    def __init__(self, nome, indirizzo, eta, scuola, media_voti):
        super().__init__(nome, indirizzo, eta)
        self.__scuola = scuola
        self.__media_voti = media_voti

    def __str__(self):
        return f"{super().__str__()}, scuola: {self.__scuola}, media voti: {self.__media_voti}"
    
    @property
    def scuola(self):
        return self.__scuola
    
    @property
    def media_voti(self):
        return self.__media_voti
    
    @scuola.setter
    def scuola(self,val):
        self.__scuola = val

    @media_voti.setter
    def media_voti(self,val):
        self.__media_voti = val

class Lavoratore(Persona):
    def __init__(self, nome, indirizzo, eta, azienda, stipendio):
        super().__init__(nome, indirizzo, eta)
        self.__azienda = azienda
        self.__stipendio = stipendio

    def __str__(self):
        return f"{super().__str__()}, azienda: {self.__azienda}, stipendio: {self.__stipendio}"

    @property
    def azienda(self):
        return self.__azienda
    
    @property
    def stipendio(self):
        return self.__stipendio
    
    @azienda.setter
    def azienda(self,val):
        self.__azienda = val

    @stipendio.setter
    def stipendio(self,val):
        self.__stipendio = val

persona1 = Persona("Giada", "Cumiana", 17)
studente1 = Studente("Marco", "Piossasco", 85, "Airasca", 10)
lavoratore1 = Lavoratore("Teresa", "Pinerolo", 12, "Bau INC", 10000)

lavoratore2 = Lavoratore(persona1.nome, persona1.eta, persona1.indirizzo, "Miao INC", 50506)

print(persona1)
print(studente1)
print(lavoratore1)
print(lavoratore2)