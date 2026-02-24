""" Funzion in Python """

# Importante che i default arguments si trovino in fondo e mai all'inizio. L'assegnazione del valore è posizionale

def presentazione (nome, cognome, hobby = "eating pizza"):
    print(f"Benvenuto {nome} {cognome}, sono felice che il tuo hobby sia {hobby}")
presentazione("pitt", "brad")