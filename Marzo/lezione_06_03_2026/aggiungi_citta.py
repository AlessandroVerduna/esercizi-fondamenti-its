""" Aggiungere città mediante Python"""

import sqlite3

while True:
    regione = input("Inserisci il nome della regione [premi q per uscire]: ")
    if regione.lower() == "q":
        break
    capoluogo = input("Inserisci il nome del capoluogo di regione: ")

    query = "insert into regioni (nome, capoluogo) values (?,?);"
    values = (regione, capoluogo)

    db = sqlite3.Connection("regioni.db")

    cursor = db.cursor()

    cursor.execute(query, values)

    db.commit()

    print("Recordo inserito con successo!")
