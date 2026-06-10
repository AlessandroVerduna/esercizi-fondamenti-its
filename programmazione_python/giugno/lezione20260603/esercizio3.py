"""
Autore: Alessandro Verduna
Data: 03/06/2026

Consegna: Terzo Esercizio
    Progetta una classe che legga un file di testo.
    Tale classe deve avere un metodo che restituisca la parola con frequenza maggiore.
    [Suggerimento: usare un dizionario per contare le occorrenze]
    Provare il programma con testi classici come la Divina Commedia.
"""

class GestioneFile(object):
    """
    Classe che gestisce la lettura di un file di testo e l'analisi
    delle parole contenute al suo interno.
    """

    def __init__(self):
        """Costruttore di default (vuoto)."""
        pass

    def parolaPiuFrequente(self):
        """
        Legge il file 'racconto.txt', calcola la frequenza di ogni parola
        e stampa la parola più frequente.
        """
        # Lettura del file di input
        with open("racconto.txt", "r", encoding="utf-8") as file:
            contenuto = file.read()
            parole = contenuto.split()

        # Conteggio delle frequenze tramite dizionario
        conteggi = {}
        for parola in parole:
            if parola not in conteggi:
                conteggi[parola] = 1
            else:
                conteggi[parola] += 1

        # Individuazione della parola più frequente
        piu_frequente = max(conteggi, key=conteggi.get)

        # Stampa del risultato
        print(piu_frequente)


# Istanziazione della classe e prova del metodo
file = GestioneFile()
file.parolaPiuFrequente()
