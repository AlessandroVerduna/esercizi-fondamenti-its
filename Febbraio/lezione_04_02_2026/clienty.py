clienti = []

f = open("clienti.txt", "r")

for riga in f:
    riga = riga.replace("\n", "")
    riga = riga.replace(" ", "")
    riga = riga.strip()
    if riga != "":
        clienti.append(riga)
f.close()

f = open('clienti.sql', 'w')

for cliente in clienti:
    pezzo = cliente.split(",")
    first_name = pezzo[0]
    last_name = pezzo[1]
    phone = pezzo[2]
    email = pezzo[3]
    address = pezzo[4]
    city = pezzo[5]
    province = pezzo[6]
    region = pezzo[7]
    postal_code = pezzo[8]
    registration_date = pezzo[9]
    f.write(f"insert into customers (first_name, last_name, phone, email, address, city, province, region, registration_date) values ('{first_name}', '{last_name}', '{phone}', '{email}', '{address}', '{city}', '{province}', '{region}', '{registration_date}');\n")
f.close()