import os, json, random, datetime, csv, re, math, statistics, shutil

from dataclasses import dataclass, field

# 0. Preparazione (sys, pathlib, os)
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

# 2. Generazione studenti casuali (random, datetime)
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
    voti: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.nome = random.choice(nomi)
        self.cognome = random.choice(["Bianchi", "Rossi"])
        self.data_nascita = datetime.date(random.randint(2004,2006), random.randint(1,12), random.randint(1,28))
        self.email = f"{(self.nome).lower()}.{(self.cognome).lower()}@scuola.it"
        self.voti = {m: random.randint(voto_min, voto_max) for m in materie}
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "data_nascita": str(self.data_nascita),
            "email": self.email,
            "voti": self.voti
        }

studenti = [Studente(id=i+1) for i in range(numero_studenti)]

studenti_dict = [s.to_dict() for s in studenti]

with open("studenti.json", "w", encoding="utf-8") as f:
    json.dump(studenti_dict, f, indent=4, ensure_ascii=False)


# 3. Salvataggio su CSV (csv)
ora_corrente = "_20-04-2026_12-00"
# ora_corrente = datetime.datetime.now()
# ora_corrente = ora_corrente.strftime('_%d-%m-%Y_%H-%M')

with open(f"data/input/studenti{ora_corrente}.csv", "w", encoding="utf-8") as f:
    campi = ["id", "nome", "cognome", "data_nascita", "email", "matematica", "informatica", "italiano"]
    writer = csv.DictWriter(f, fieldnames=campi)
    
    writer.writeheader()
    righe_csv = []
    for stud in studenti:
        base = {
            "id": stud.id,
            "nome": stud.nome,
            "cognome": stud.cognome,
            "data_nascita": str(stud.data_nascita),
            "email": stud.email
        }

        # aggiungi i voti come colonne separate
        for materia in materie:
            base[materia.lower()] = stud.voti[materia]

        righe_csv.append(base)

    writer.writerows(righe_csv)


# 4. Leggi il file CSV e valida i campi
with open(f"data/input/studenti{ora_corrente}.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    pattern_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    pattern_data = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

    lista_scartati = []
    lista_validi = []
    email_non_valida = 0
    data_non_valida = 0

    for riga in reader:
        if re.match(pattern_email, riga["email"]) is None:
            email_non_valida += 1
            lista_scartati.append(riga)
        elif re.match(pattern_data, riga["data_nascita"]) is None:
            data_non_valida += 1
            lista_scartati.append(riga)
        else:
            lista_validi.append(riga)
    print(f"Numero email non valide: {email_non_valida} e numero date non valide {data_non_valida}")

# 5. Conversione CSV → JSON (json)
with open("data/output/studenti_validi.json", "w", encoding="utf-8") as f:
    json.dump(lista_validi, f, indent=4, ensure_ascii=False)

# 6. Calcolo statistiche per materia (statistics, math)
with open("data/output/studenti_validi.json", "r", encoding="utf-8") as f:
    studenti = json.load(f)
    matematica = []
    informatica = []
    italiano = []

    for studente in studenti:
        matematica.append(int(studente['matematica']))
    media_mat = statistics.mean(matematica)
    median_mat = statistics.median(matematica)
    stdev_mat = statistics.stdev(matematica)
    min_mat = min(matematica)
    max_mat = max(matematica)

    for studente in studenti:
        informatica.append(int(studente['informatica']))
    media_inf = statistics.mean(informatica)
    median_inf = statistics.median(informatica)
    stdev_inf = statistics.stdev(informatica)
    min_inf = min(informatica)
    max_inf = max(informatica)

    for studente in studenti:
        italiano.append(int(studente['italiano']))
    media_ita = statistics.mean(italiano)
    median_ita = statistics.median(italiano)
    stdev_ita = statistics.stdev(italiano)
    min_ita = min(italiano)
    max_ita = max(italiano)

    with open("statistiche.json", "w", encoding="utf-8") as f:   
        json.dump({
            "matematica": {
                "media": media_mat,
                "mediana": median_mat,
                "min": min_mat,
                "max": max_mat,
                "stdev": stdev_mat
            },
            "informatica": {
                "media": media_inf,
                "mediana": median_inf,
                "min": min_inf,
                "max": max_inf,
                "stdev": stdev_inf
            },
            "italiano": {
                "media": media_ita,
                "mediana": median_ita,
                "min": min_ita,
                "max": max_ita,
                "stdev": stdev_ita
            }
        }, f, indent=4, ensure_ascii=False)
    
# 7. Classifica migliori studenti (collections)
with open("data/output/studenti_validi.json", "r", encoding="utf-8") as f:
    studenti = json.load(f)

    for studente in studenti:
        media = [
            int(studente["matematica"]),
            int(studente["informatica"]),
            int(studente["italiano"])
        ]
        media_personale = statistics.mean(media)
        studente["media"] = media_personale

    lista_medie = []

    for studente in studenti:
        lista_medie.append([studente["media"], studente])

    top_5 = lista_medie[:5]
    with open("data/output/studenti_top5.txt", "w", encoding="utf-8") as f:
        for media, studente in top_5:
            f.write(f"{studente["nome"]}, {studente["cognome"]}, {round(media, 2)} \n")

# 8. Report finale (json + txt)
oggi_data = datetime.datetime.now().strftime('%Y-%m-%d')
with open(f"report/report_{oggi_data}.txt", "w", encoding="utf-8") as f:
    f.write("prova")

# 9. Backup automatico (os, pathlib)
shutil.copy(f"data/input/studenti{ora_corrente}.csv", f"data/backup/backup_studenti{ora_corrente}.csv")

# 10. Gestione CLI (sys)
