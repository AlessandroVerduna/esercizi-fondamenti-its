#list unpacking

class Studente:
    def __init__(self, nome, cognome, valutazione):
        self.nome = nome
        self.cognome = cognome
        self.valutazione = valutazione
        
    def __str__(self):
        return f"{self.nome}, {self.cognome}, - Valutazione {self.valutazione}"
        
#list

studenti = []

# record1 = ["Pietro", "Rossi", 28]

# nome, cognome, valutazione = record1

nome, cognome, valutazione = ["Pietro", "Rossi", 28]

# nome = record1[0]
# cognome = record1[1]
# valutazione = record1[2]

# stud1 = Studente(nome, cognome, valutazione)

# studenti.append(stud1)

studenti.append(Studente(nome, cognome, valutazione))

for i in studenti:
    print(i)