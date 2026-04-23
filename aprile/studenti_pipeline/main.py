import os,json, random, datetime

from dataclasses import dataclass

# 0. Preparazione (sys, pathlib, os)
def inizializzazione_cartelle():
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists("report"):
        os.mkdir("report")
    if not os.path.exists("data/input"):
        os.mkdir("data/input")
    if not os.path.exists("data/output"):
        os.mkdir("data/output")
    if not os.path.exists("data/backup"):
        os.mkdir("data/backup")

# 1. File di configurazione (json)
def inizializzazione_json():
    DEFAULT_CONFIG = {
    "numero_studenti": 20,
    "voto_min": 1,
    "voto_max": 10,
    "materie": ["Matematica", "Informatica", "Italiano"],
    "classe": "5A",
    "nomi": ["Mario", "Gianni", "Alessandro", "Pippo", "Sara"]
    }  
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)

# 2. Generazione studenti casuali 
def generazione_studenti_casuali():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    numero_studenti = config["numero_studenti"]
    voto_min = config["voto_min"]
    voto_max = config["voto_max"]
    materie = config["materie"]
    classe = config["classe"]
    nomi = config["nomi"]

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

    # 3. Generazione studenti
    studenti = [
        Studente.genera(i + 1, nomi, voto_min, voto_max, materie)
        for i in range(numero_studenti)
    ]

    # 4. Salvataggio JSON
    studenti_dict = [s.to_dict() for s in studenti]

    with open("studenti.json", "w", encoding="utf-8") as f:
        json.dump(studenti_dict, f, indent=4, ensure_ascii=False)

def main():
    inizializzazione_cartelle()
    inizializzazione_json()
    generazione_studenti_casuali()

if __name__ == "__main__":
    main()