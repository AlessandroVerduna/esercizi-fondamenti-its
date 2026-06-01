"""
Autore: Alessandro Verduna
Data: 29/05/2026

Consegna: Quarto Esercizio
    Si definisca una classe Persona che abbia gli attributi:
        - nome
        - indirizzo
        - età
    La classe deve contenere:
        - costruttore
        - overriding del metodo __str__
        - getter e setter per tutti gli attributi

    Derivare dalla classe Persona:
        - Studente (attributi aggiuntivi: scuola, media voti)
        - Lavoratore (attributi aggiuntivi: azienda, stipendio)

    Aggiungere getter e setter per gli attributi aggiuntivi.
    Effettuare overriding di costruttori e __str__.
    Provare le tre classi istanziando almeno un oggetto per classe.
"""

class Persona(object):
    """
    Classe base che rappresenta una persona con nome, indirizzo ed età.
    Gli attributi sono privati e gestiti tramite property.
    """

    def __init__(self, nome, indirizzo, eta):
        """
        Costruttore della classe Persona.

        Parametri:
            nome (str): nome della persona.
            indirizzo (str): indirizzo di residenza.
            eta (int): età della persona.
        """
        self.__nome = nome
        self.__indirizzo = indirizzo
        self.__eta = eta

    def __str__(self):
        """Restituisce una rappresentazione leggibile dell'oggetto."""
        return f"Nome: {self.nome}, età: {self.eta}, indirizzo: {self.indirizzo}"

    # Getter
    @property
    def nome(self):
        return self.__nome

    @property
    def indirizzo(self):
        return self.__indirizzo

    @property
    def eta(self):
        return self.__eta

    # Setter
    @nome.setter
    def nome(self, val):
        self.__nome = val

    @indirizzo.setter
    def indirizzo(self, val):
        self.__indirizzo = val

    @eta.setter
    def eta(self, val):
        self.__eta = val


class Studente(Persona):
    """
    Classe derivata che rappresenta uno studente.
    Aggiunge gli attributi scuola e media voti.
    """

    def __init__(self, nome, indirizzo, eta, scuola, media_voti):
        """
        Costruttore ridefinito per aggiungere gli attributi dello studente.
        """
        super().__init__(nome, indirizzo, eta)
        self.__scuola = scuola
        self.__media_voti = media_voti

    def __str__(self):
        """Restituisce una rappresentazione leggibile dell'oggetto Studente."""
        return f"{super().__str__()}, scuola: {self.__scuola}, media voti: {self.__media_voti}"

    # Getter
    @property
    def scuola(self):
        return self.__scuola

    @property
    def media_voti(self):
        return self.__media_voti

    # Setter
    @scuola.setter
    def scuola(self, val):
        self.__scuola = val

    @media_voti.setter
    def media_voti(self, val):
        self.__media_voti = val


class Lavoratore(Persona):
    """
    Classe derivata che rappresenta un lavoratore.
    Aggiunge gli attributi azienda e stipendio.
    """

    def __init__(self, nome, indirizzo, eta, azienda, stipendio):
        """
        Costruttore ridefinito per aggiungere gli attributi del lavoratore.
        """
        super().__init__(nome, indirizzo, eta)
        self.__azienda = azienda
        self.__stipendio = stipendio

    def __str__(self):
        """Restituisce una rappresentazione leggibile dell'oggetto Lavoratore."""
        return f"{super().__str__()}, azienda: {self.__azienda}, stipendio: {self.__stipendio}"

    # Getter
    @property
    def azienda(self):
        return self.__azienda

    @property
    def stipendio(self):
        return self.__stipendio

    # Setter
    @azienda.setter
    def azienda(self, val):
        self.__azienda = val

    @stipendio.setter
    def stipendio(self, val):
        self.__stipendio = val

persona1 = Persona("Giada", "Cumiana", 17)
studente1 = Studente("Marco", "Piossasco", 18, "Airasca", 10)
lavoratore1 = Lavoratore("Teresa", "Pinerolo", 32, "Bau INC", 10000)

lavoratore2 = Lavoratore(persona1.nome, persona1.indirizzo, persona1.eta, "Miao INC", 50506)

print(persona1)
print(studente1)
print(lavoratore1)
print(lavoratore2)