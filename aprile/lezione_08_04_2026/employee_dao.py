import database
from dataclasses import dataclass

@dataclass
class Impiegato:
    nome: str
    cognome: str
    ruolo: str

    def __str__(self):
        return f"{self.nome} {self.cognome} - {self.ruolo}"

class EmployeeDao:
    def findImpiegati(self):
        tabella_impiegati = database.connetti()
        impiegati = database.interroga(tabella_impiegati, "select FirstName, lastname, title from employee;")
        
        return [Impiegato(n,c,r) for n,c,r, in impiegati]

# tabella_impiegati = database.connetti()

# impiegati = database.interroga(tabella_impiegati, "select a.FirstName, a.LastName, a.Title from employee a;")

# scatola = [Impiegato(n,c,r) for n, c, r in impiegati]

# print(scatola)