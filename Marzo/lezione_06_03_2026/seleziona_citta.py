import sqlite3

query = "select * from regioni;"

db = sqlite3.connect("regioni.db")

cursor = db.cursor()

cursor.execute(query)

result = cursor.fetchall()

for i in result:
    print(f"Il capoluogo della regione {i[1]} è: {i[2]}")

#print(result)