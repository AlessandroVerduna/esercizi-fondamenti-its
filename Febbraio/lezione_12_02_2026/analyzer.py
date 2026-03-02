""" Analizzatore di oggetti """

def analizza(collezione):
    print("Tipo del dato ", type(collezione))
    print("# elementi", len(collezione))
    print("Metodi disponibili ", help(collezione))