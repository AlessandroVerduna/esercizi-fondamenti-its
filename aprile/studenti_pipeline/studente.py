import datetime, random
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    cognome: str
    data_nascita: datetime.date
    email: str
    voti: dict

    @classmethod
    def genera(cls, id_studente, nomi, voto_min, voto_max, materie):
        nome = random.choice(nomi)
        cognome = random.choice(["Bianchi", "Rossi"])
        data_nascita = datetime.date(
            random.randint(2004, 2006),
            random.randint(1, 12),
            random.randint(1, 28)
        )
        email = f"{nome.lower()}.{cognome.lower()}@scuola.it"
        voti = {m: random.randint(voto_min, voto_max) for m in materie}

        return cls(
            id=id_studente,
            nome=nome,
            cognome=cognome,
            data_nascita=data_nascita,
            email=email,
            voti=voti
        )

    def to_dict(self):
        return {
        "id": self.id,
        "nome": self.nome,
        "cognome": self.cognome,
        "data_nascita": str(self.data_nascita),
        "email": self.email,
        "voti": self.voti
        }