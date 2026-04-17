import csv


def leggi_file_csv():
    with open("auto.csv", mode="r", newline="", encoding="utf-8") as f:
        # reader = csv.reader(f)
        # reader = csv.DictReader(f)

        # marche = list()
        # marche = [row.get("Marca", "Nessuna") for row in reader]
        # for row in reader:
        #     marche.append(row.get("Marca", "Nessuna"))
        # print(marche)

        reader = csv.DictReader(f)

        return list(reader)




moto = leggi_file_csv("moto.csv")

for m in moto:
    print(m['Modello'])

print("*" * 25)

auto = leggi_file_csv("auto.csv")

for a in auto:
    print(a['Modello'])