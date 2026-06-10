"""
Autore: Alessandro Verduna
Data: 03/06/2026

Consegna: Secondo Esercizio
    Scrivi una classe che legga un file di testo e stampi sul file “output.txt”
    la parola più lunga contenuta.
    [Facoltativo: prime N parole più lunghe — NON richiesto in questa versione]
    Istanziare la classe e provare i metodi implementati.
"""

class GestioneFile(object):
    """
    Classe che gestisce la lettura di un file di testo e l'estrazione
    della parola più lunga contenuta.
    """

    def __init__(self):
        """Costruttore di default (vuoto)."""
        pass

    def parolaLunga(self):
        """
        Legge il file 'input.txt', individua la parola più lunga
        e la salva nel file 'output.txt'.
        """
        # Lettura del file di input
        with open("input.txt", "r", encoding="utf-8") as file:
            contenuto_raw = file.read()
            parole = contenuto_raw.split()

        # Individuazione della parola più lunga
        parola_massima = max(parole, key=len)

        # Scrittura nel file di output
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(parola_massima)


# Istanziazione della classe e prova del metodo
file = GestioneFile()
file.parolaLunga()
