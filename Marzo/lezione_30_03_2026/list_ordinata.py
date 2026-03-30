from dataclasses import dataclass

@dataclass
class Libro:
    titolo: str
    autore: str
    pagine: int
    
def ordinatore_titoli(libro):
    return libro.titolo
    
libri = [
    Libro("A nord di Ushaia", "Bogliaccino", 500),
    Libro("E oggi è ancora bello", "Gian Marco", 300),
    Libro("Bisogna saper perdere", "Gian Marco", 240)
]

libri.sort(key = lambda libro:libro.pagine)

print(libri)

voti =  [25, 28, 27, 26, 29, 18]

parole = ["Pisolo", "Mammolo", "Brontolo"]

daordinare = [25,28,24,27,29,29,24]

ordinata= []

minore = max(daordinare) + 1

while True:
    for i in daordinare:
        if i < minore:
            minore = i
    ordinata.append(minore)
    daordinare.remove(minore)
    if not daordinare:
        break
    minore = max(daordinare) + 1 

print(ordinata)