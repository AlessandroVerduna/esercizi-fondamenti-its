""" Database città """

# import json

# Qui hai solo text, ha meno cose, ha meno tipi
import sqlite3

regioni = {
    "Piemonte": ["Torino", "Alessandria"],
    "Liguria": ["Genova", "Rapallo"],
    "Lombardia": ["Milano", "Como"]
}

# regionipy = json.dumps(regioni)

# regionijson = json.loads(regionipy)

# print(regionipy)

# print(regionijson)

db = sqlite3.connect("regioni.db")

cursor = db.cursor()

query = """

create table if not exists regioni(
    regione_id integer primary key autoincrement,
    nome text not null,
    capoluogo text not null
);

"""

for regione in regioni:
    query = f"insert into regioni (nome, capoluogo) values ('{regione}', '{regioni.get(regione)[0]}');"
    cursor.execute(query)


db.commit()