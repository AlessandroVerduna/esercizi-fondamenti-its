ordini = []

f = open("ordini.txt", "r")

for riga in f:
    riga = riga.replace("\n", "")
    #riga = riga.remove(" ")
    riga = str(riga)
    riga = riga.strip()
    riga = riga.replace("\t", "")
    if riga != "":
        ordini.append(riga)

f.close()

f = open("ordini.sql", "w")

for a in ordini:
    i = [x.strip() for x in a.split(",")]
    order_data = i[0]
    total = i[1]
    shipping = i[2]
    shipping_address = i[3]
    customer_id = i[4]
    f.write(f"insert into orders (order_data, total, shipping, shipping_address, customer_id) values ('{order_data}', {total} ,'{shipping}', '{shipping_address}', {customer_id});\n")

f.close()