ordini = []

f = open("books.txt", "r")

for riga in f:
    riga = riga.replace("\n", "")
    #riga = riga.remove(" ")
    riga = str(riga)
    riga = riga.strip()
    riga = riga.replace("\t", "")
    if riga != "":
        ordini.append(riga)

f.close()

f = open("books.sql", "w")

for a in ordini:
    i = [x.strip() for x in a.split(",")]
    isbn = i[0]
    title = i[1]
    price = i[2]
    price_vat = i[3]
    pages = i[4]
    editor_id = i[5]
    f.write(f"insert into books (isbn, title, price, price_vat, pages, editor_id) values ('{isbn}', '{title}' ,{price}, {price_vat}, {pages}, {editor_id});\n")

f.close()