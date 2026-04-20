import os, json, random, datetime, csv, re

from dataclasses import dataclass, field

# Creazione albero cartelle
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

# Crea fle JSON
if not os.path.exists("config.json"):
    with open("config.json", "w", encoding="utf-8") as f:
        f.write("""    {
        "numero_studenti": 4,
        "voto_min": 2,
        "voto_max": 10,
        "materie": ["Matematica", "Informatica", "Italiano"],
        "classe": "5A",
        "nomi": ["Mario", "Gianni", "Alessandro", "Pippo", "Sara"]
    }""")

# Genera studenti casuali
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    #print(config)
    
elementi = []
for chiave, valore in config.items():
    elementi += [valore]
        
numero_studenti = elementi[0]
voto_min = elementi[1]
voto_max = elementi[2]
materie = elementi[3]
classe = elementi[4]
nomi = elementi[5]
#print(numero_studenti)

@dataclass
class Studente:
    id: int = None
    nome: str = None
    cognome: str = None
    data_nascita: datetime.date = None
    email: str = None
    #voti: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.nome = random.choice(nomi)
        self.cognome = random.choice(["Bianchi", "Rossi"])
        self.data_nascita = datetime.date(random.randint(2004,2006), random.randint(1,12), random.randint(1,28))
        self.email = f"{(self.nome).lower()}.{(self.cognome).lower()}@scuola.it"
        # self.id = 
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "data_nascita": str(self.data_nascita),
            "email": self.email
        }

studenti = [Studente(id=i+1) for i in range(numero_studenti)]

studenti_dict = [s.to_dict() for s in studenti]

with open("studenti.json", "w", encoding="utf-8") as f:
    json.dump(studenti_dict, f, indent=4, ensure_ascii=False)


# Salva un file CSV
ora_corrente = "_20-04-2026_12-00"
# ora_corrente = datetime.datetime.now()
# ora_corrente = ora_corrente.strftime('_%d-%m-%Y_%H-%M')

with open(f"data/input/studenti{ora_corrente}.csv", "w", encoding="utf-8") as f:
    campi = ["id", "nome", "cognome", "data_nascita", "email"]
    writer = csv.DictWriter(f, fieldnames=campi)
    
    writer.writeheader()
    writer.writerows(studenti_dict)

# Leggi il file CSV e valida i campi
with open(f"data/input/studenti{ora_corrente}.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    pattern_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    
    for riga in reader:
        print(riga["email"])
        if re.match(pattern_email, riga["email"]) is not None:
            print("Good job!")
        else:
            print("Svegliati")