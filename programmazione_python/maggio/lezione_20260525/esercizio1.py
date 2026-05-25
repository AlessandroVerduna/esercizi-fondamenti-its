"""
Autore: Alessandro Verduna
Data: 25/05/2026

Consegna: Primo Esercizio
    Creare una classe Insegnante con attributi nome, età e stipendio, dove stipendio deve
    essere un attributo privato.
    Costruire tutti i metodi getter e setter per gli attributi (anche per quelli pubblici).
    Effettuare l'overriding del metodo __str__ in maniera tale che restituisca gli attributi nome e
    età.
    Provare la classe istanziando almeno due oggetti.
"""

class Insegnante(object):
    """
    Classe che rappresenta un insegnante, con attributi nome, età e stipendio.
    Lo stipendio è gestito come attributo privato.
    """

    def __init__(self, nome, eta, stipendio):
        """
        Inizializza un nuovo oggetto Insegnante.

        Parametri:
            nome (str): nome dell'insegnante.
            eta (int): età dell'insegnante.
            stipendio (float/int): stipendio dell'insegnante (privato).
        """
        self.nome = nome
        self.eta = eta
        self.__stipendio = stipendio

    # Getter pubblici
    def getNome(self):
        """Restituisce il nome dell'insegnante."""
        return self.nome

    def getEta(self):
        """Restituisce l'età dell'insegnante."""
        return self.eta

    @property
    def stipendio(self):
        """Restituisce lo stipendio (attributo privato)."""
        return self.__stipendio

    # Setter pubblici
    def setNome(self, val):
        """Imposta un nuovo valore per il nome."""
        self.nome = val

    def setEta(self, val):
        """Imposta un nuovo valore per l'età."""
        self.eta = val

    @stipendio.setter
    def stipendio(self, val):
        """Imposta un nuovo valore per lo stipendio (privato)."""
        self.__stipendio = val

    def __str__(self):
        """
        Restituisce una rappresentazione leggibile dell'oggetto,
        mostrando solo nome ed età.
        """
        return f"Nome: {self.nome}, età: {self.eta}"


# Istanziazione di almeno due oggetti come richiesto dalla consegna
insegnante1 = Insegnante("Giada", 25, 100)
insegnante2 = Insegnante("Marco", 75, 500)

print(insegnante1)
print(insegnante2)
