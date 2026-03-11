""" Class che rappresenmta il punto sul piano cartesiano """

class Punto:
    def __init__(self, x : int, y : int): # questo lo chiamiamo METHOD ovvero una funzione dentro una classe
        self.x = x
        self.y = y
        #print(f"Ho creato un nuovo punto di coordinate ({self.x},{self.y})")
    
    def __str__(self):
        return f"Ho creato un nuovo punto di coordinate: ({self.x},{self.y})"