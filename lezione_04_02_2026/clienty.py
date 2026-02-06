clienti = []

f = open("clienti.txt", "r")

for riga in f:
    riga = riga.replace("\n", "")
    # riga = riga.replace("\t", ",")
    riga = riga.strip()
    if riga != "":
        clienti.append(riga)
f.close()

f = open('clienti.sql', 'w')

for cliente in clienti:
    pezzo = cliente.split(",")
    first_name = pezzo[0]
    last_name = pezzo[1]
    email = pezzo[2]
    address = pezzo[3]
    city = pezzo[4]
    province = pezzo[5]
    region = pezzo[6]
    registration_date = pezzo[7]
    f.write(f"insert into customers (first_name, last_name, email, address, city, province, region, registration_date) values ('{first_name}', '{last_name}', '{email}', '{address}', '{city}', '{province}', '{region}', '{registration_date}');\n")
f.close()