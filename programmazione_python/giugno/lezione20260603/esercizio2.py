"""
    Autore: Alessandro Verduna
    Data: 03/06/2026

    Consegna: Secondo Esercizio
        Scrivi una classe che legga un file di testo e stampi sul file: “output.txt” la parola più lunga
        contenuta. [Facoltativo: stampi sul file: “output.txt” le prime N parole più lunghe, N è dato
        in input dall'utente].
        Istanziare la classe e provare i metodi implementati
"""

class GestioneFile(object):
    def __init__(self):
        pass

    def parolaLunga(self):
        with open ("input.txt", "r", encoding="utf-8") as file:
            contenuto = []
            
            contenuto_raw = file.read()

            contenuto = contenuto_raw.split()

        with open ("output.txt", "w", encoding="utf-8") as file:
            risultato = max(contenuto)
            
            file.write(risultato)
    
file = GestioneFile()
file.parolaLunga()