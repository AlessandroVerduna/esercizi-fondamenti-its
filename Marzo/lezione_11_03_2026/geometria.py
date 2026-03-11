from punto import Punto
from segmento import Segmento
from traingolo import Triangolo

a = Punto(2,2)
b = Punto(6,2)
c = Punto(2,5)

print(a)
print(b)
print(c)

ab = Segmento(a,b)
ac = Segmento(a,c)
bc = Segmento(b,c)

print(f"La lunghezza del segmento AB è: {ab.lunghezza()}")
print(f"La lunghezza del segmento AC è: {ac.lunghezza()}")
print(f"La lunghezza del segmento BC è: {bc.lunghezza()}")

t1 = Triangolo(a,b,c)

print(t1.perimetro())
print(t1.area())
print(t1)