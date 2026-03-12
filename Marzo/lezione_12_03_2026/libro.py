""" Classe libro, rappresenta un libro del database """

class Libro:
    def __init__(self, libroId, collocazione, autore, titolo, editore, classificazione):
        self.libroId = libroId
        self.collocazione = collocazione
        self.autore = autore
        self.titolo = titolo
        self.editore = editore
        self.classficazione = classificazione
    
    def __str__(self):
        return f""" Titolo: {self.titolo}, 
                    autore: {self.autore},
                    editore: {self.editore}, 
                    collocazione: {self.collocazione}
                """
    def toHtml(self):
        return f"""
                    <div>
                        <h2>Titolo: {self.titolo}</h2>
                    </div>
                """