# libri = [
#     ['L\'uomo ragno', 120, 15, 2],
#     ['La donna ragno', 150, 25, 2],
#     ['Il bambino ragno', 220, 35, 2],
#     ['L\'insetto ragno', 80, 10, 1],
#     ['L\'opossum grigio', 320, 45, 1]
# ]

source = open("libri.csv", "r")

libri = []

for riga in source:
    riga_splittata = riga.split(",")
    titolo = riga_splittata[0].replace('"', '')
    pagine = int(riga_splittata[2].replace('"', ''))
    prezzo = float(riga_splittata[4].replace('"', ''))
    print(f"Il libro {titolo} ha {pagine} pagine e costa ${prezzo}")
    libri.append([titolo, pagine, prezzo, 1])
source.close()


f = open("insert_libri.sql", "w")

f.write("use its2026;\n\n")

for libro in libri:
    #print(libro)
    titolo = str(libro[0]).replace("'", "\\'")
    pagine = libro[1]
    prezzo = libro[2]
    editore_id = libro[3]
    f.write(f"INSERT INTO libri SET titolo = '{titolo}', pagine = {pagine}, prezzo = {prezzo}, editore_id = {editore_id};\n")

f.close()