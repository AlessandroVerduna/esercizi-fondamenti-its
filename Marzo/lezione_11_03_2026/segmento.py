""" Class che rappresenta un segmento """

from punto import Punto
from math import sqrt, pow

# class Segmento:
#     def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int):
#         self.x1 = x1 
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         print(f"Segmento creato con estremi ({x1},{y1}) e ({x2},{y2})")

class Segmento:
    def __init__(self, a : Punto,b : Punto):
        self.a = a
        self.b = b
    
    def lunghezza(self):
        return sqrt(pow(self.b.x - self.a.x,2) + pow(self.b.y - self.a.y,2))