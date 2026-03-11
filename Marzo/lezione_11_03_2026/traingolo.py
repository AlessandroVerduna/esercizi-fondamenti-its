from punto import Punto
from segmento import Segmento
from math import sqrt

class Triangolo:
    def __init__(self, a: Punto, b: Punto, c: Punto):
        self.a = a
        self.b = b
        self.c = c
        
        self.ab = Segmento(a,b)
        self.ac = Segmento(a,c)
        self.bc = Segmento(b,c)
    
    def perimetro(self):
        return self.ab.lunghezza() + self.ac.lunghezza() + self.bc.lunghezza()
    
    def area(self):
        sp = self.perimetro() / 2
        return sqrt(sp * (sp - self.ab.lunghezza()) * (sp - self.ac.lunghezza()) * (sp - self.bc.lunghezza()))
    
    def __str__(self):
        return f"Il perimetro di questo triangolo è {self.perimetro():.2f}, l'area di questo triangolo è: {self.area():.2f}"