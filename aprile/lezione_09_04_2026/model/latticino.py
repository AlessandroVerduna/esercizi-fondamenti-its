class Latticino:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def __str__(self):
        return f"{self.nome} ({self.peso} kg)"

class Mozzarella(Latticino):
    def __init__(self, nome, peso, tipo):
        super().__init__(nome, peso)
        self.tipo = tipo

cacio = Latticino("Cacio", 1)
m1 = Mozzarella("Ciliegino", 0.2, "Bufala")

print(cacio)
print(m1)