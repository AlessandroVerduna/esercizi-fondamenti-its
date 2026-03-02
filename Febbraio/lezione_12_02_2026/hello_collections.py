""" Strutture dati: list, tuple, set, dict """

def analizza(collezione):
    print("Tipo del dato ", type(voti))
    print("# elementi", len(voti))
    print("Metodi disponibili ", help(voti))


# list
voti = [25, 29, 26]
#analizza(voti)

# tuple
voti = (25, 29, 26)
#analizza(voti)

# set
voti = {25, 29, 26}
#analizza(voti)

# dict 
voti = {
    "python" : 25,
    "java" : 29,
    "c#" : 26
}
analizza(voti)