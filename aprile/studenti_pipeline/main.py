import os,json, datetime, csv, re, statistics, shutil, sys, textwrap

from dataclasses import dataclass
from studente import Studente

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
    "materie": ["matematica", "informatica", "italiano"],
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

    studenti = [
        Studente.genera(i + 1, nomi, voto_min, voto_max, materie)
        for i in range(numero_studenti)
    ]

    studenti_dict = [s.to_dict() for s in studenti]

    with open("studenti.json", "w", encoding="utf-8") as f:
        json.dump(studenti_dict, f, indent=4, ensure_ascii=False)

# 3. Salvataggio su CSV
def salvataggio_csv():
    ora_corrente = "_20-04-2026_12-00"
    # ora_corrente = datetime.datetime.now()
    # ora_corrente = ora_corrente.strftime('_%d-%m-%Y_%H-%M')

    with open("studenti.json", "r", encoding="utf-8") as f:
        studenti = json.load(f)

    with open(f"data/input/studenti{ora_corrente}.csv", "w", encoding="utf-8") as f:
        campi = ["id", "nome", "cognome", "data_nascita", "email", "matematica", "informatica", "italiano"]
        writer = csv.DictWriter(f, fieldnames=campi)

        writer.writeheader()
        righe_csv = []
        materie = ["matematica", "informatica", "italiano"]
        for stud in studenti:
            base = {
                "id": stud["id"],
                "nome": stud["nome"],
                "cognome": stud["cognome"],
                "data_nascita": stud["data_nascita"],
                "email": stud["email"]
            }

            for materia in materie:
                base[materia] = stud["voti"][materia]

            righe_csv.append(base)

        writer.writerows(righe_csv)

# 4. Leggi il file CSV e valida i campi
def leggi_e_controlla_csv():
    ora_corrente = "_20-04-2026_12-00"
    # ora_corrente = datetime.datetime.now()
    # ora_corrente = ora_corrente.strftime('_%d-%m-%Y_%H-%M')

    with open(f"data/input/studenti{ora_corrente}.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        pattern_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        pattern_data = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

        lista_scartati = []
        lista_validi = []
        email_non_valida = 0
        data_non_valida = 0
        voti_non_validi = 0

        for riga in reader:
            if re.match(pattern_email, riga["email"]) is None:
                email_non_valida += 1
                lista_scartati.append(riga)
            elif re.match(pattern_data, riga["data_nascita"]) is None:
                data_non_valida += 1
                lista_scartati.append(riga)
            elif int(riga["matematica"]) < 2 or int(riga["informatica"]) < 2 or int(riga["italiano"]) < 2:
                voti_non_validi += 1
                lista_scartati.append(riga)
            else:
                lista_validi.append(riga)
        print(f"Numero email non valide: {email_non_valida}\n Numero date non valide {data_non_valida}\n Numero scartati causa voti non validi: {voti_non_validi}")

# 5. Conversione CSV → JSON
    with open("data/output/studenti_validi.json", "w", encoding="utf-8") as f:
        json.dump(lista_validi, f, indent=4, ensure_ascii=False)
    with open("data/output/studenti_scartati.json", "w", encoding="utf-8") as f:
        json.dump(lista_scartati, f, indent=4, ensure_ascii=False)

# 6. Calcolo statistiche per materia
def statistiche():
    with open("data/output/studenti_validi.json", "r", encoding="utf-8") as f:
        studenti = json.load(f)

    risultati = {}
    materie = ["matematica", "informatica", "italiano"]

    for materia in materie:
        valori = [int(s[materia]) for s in studenti]

        risultati[materia] = {
            "media": statistics.mean(valori),
            "mediana": statistics.median(valori),
            "min": min(valori),
            "max": max(valori),
            "stdev": statistics.stdev(valori)
        }

    with open("statistiche.json", "w", encoding="utf-8") as f:
        json.dump(risultati, f, indent=4, ensure_ascii=False)


# 7. Classifica migliori studenti
def classifica_migliori():
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

# 8. Report finale
def report_finale():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    classe = config["classe"]

    with open("data/output/studenti_validi.json", "r", encoding="utf-8") as f:
        studenti_validi = json.load(f)

    numero_totale = config["numero_studenti"]
    numero_validi = len(studenti_validi)
    numero_scartati = numero_totale - numero_validi

    with open("statistiche.json", "r", encoding="utf-8") as f:
        stats = json.load(f)

    top5_path = "data/output/studenti_top5.txt"
    if os.path.exists(top5_path):
        with open(top5_path, "r", encoding="utf-8") as f:
            top5 = f.read().strip()
    else:
        top5 = "Nessun dato disponibile."

    oggi = datetime.datetime.now().strftime("%Y-%m-%d")

    contenuto = []
    contenuto.append(f"REPORT FINALE CLASSE {classe}")
    contenuto.append(f"Data generazione: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    contenuto.append("")
    contenuto.append(f"Numero studenti totali: {numero_totale}")
    contenuto.append(f"Studenti validi: {numero_validi}")
    contenuto.append(f"Studenti scartati: {numero_scartati}")
    contenuto.append("")
    contenuto.append("STATISTICHE PER MATERIA:")
    for materia, valori in stats.items():
        contenuto.append(f"  - {materia}:")
        contenuto.append(f"      media:   {round(valori['media'], 2)}")
        contenuto.append(f"      mediana: {round(valori['mediana'], 2)}")
        contenuto.append(f"      min:     {valori['min']}")
        contenuto.append(f"      max:     {valori['max']}")
        contenuto.append(f"      stdev:   {round(valori['stdev'], 2)}")
    contenuto.append("")
    contenuto.append("TOP 5 STUDENTI MIGLIORI:")
    contenuto.append(top5)

    report_path = f"report/report_{oggi}.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contenuto))

# 9. Backup automatico
def backup_automatico():
    ora_corrente = "_20-04-2026_12-00"
    # ora_corrente = datetime.datetime.now()
    # ora_corrente = ora_corrente.strftime('_%d-%m-%Y_%H-%M')
    shutil.copy(f"data/input/studenti{ora_corrente}.csv", f"data/backup/backup_studenti{ora_corrente}.csv")

# 10. Gestione CLI
def main():
    if len(sys.argv) < 2:
        print("Errore: nessun comando fornito.")
        print("Usa: python main.py [all|q]")
        return

    comando = sys.argv[1].lower()

    if comando == "all":
        print("Esecuzione completa del programma")
        inizializzazione_cartelle()
        inizializzazione_json()
        generazione_studenti_casuali()
        salvataggio_csv()
        leggi_e_controlla_csv()
        statistiche()
        classifica_migliori()
        report_finale()
        backup_automatico()

    elif comando == "report":
        print("Generazione report finale.")
        report_finale()

    elif comando == "generate":
        print("Validazione ambiente, generazione studenti in formato CSV")
        inizializzazione_cartelle()
        inizializzazione_json()
        generazione_studenti_casuali()
        salvataggio_csv()

    elif comando == "validate":
        print("Verifica intregità CSV e creazione JSON")
        leggi_e_controlla_csv()
        statistiche()
        classifica_migliori()

    else:
        print(f"Comando sconosciuto: {comando}")
        print("Comandi disponibili: all, report, generate, validate")

if __name__ == "__main__":
    main()