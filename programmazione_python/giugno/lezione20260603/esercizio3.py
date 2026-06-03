"""
    Autore: Alessandro Verduna
    Data: 03/06/2026

    Consegna: Terzo Esercizio
        Progetta una classe che legga un file di testo. Tale classe deve avere un metodo che
        restituisca la parola con frequenza maggiore. [Suggerimento: si consideri l'esercizio che
        contava le frequenze delle lettere in una stringa utilizzando i dictionary]
        Provare il programma con testi classici come la Divina Commedia di Dante Alighieri
        reperibile sul sito del progetto Gutenberg.
"""

class GestioneFile(object):
    def __init__(self):
        pass

    def parolaPiuFrequente(self):
        with open ("racconto.txt", "r", encoding="utf-8") as file:
            contenuto = file.read()
            parole = contenuto.split()

        conteggi = {}
        for parola in parole:
            if parola not in conteggi:
                conteggi[parola] = 1
            else:
                conteggi[parola] += 1

        piu_frequente = max(conteggi, key=conteggi.get)
        print(piu_frequente)

file = GestioneFile()
file.parolaPiuFrequente()