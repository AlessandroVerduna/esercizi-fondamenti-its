import mysql.connector

mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'world'
)

print("Connected to MySQL")

cursor = mycon.cursor()
query = 'select * from country;'

cursor.execute(query)

records = cursor.fetchall()

f = open("record.txt", "w")
for i in records:
    f.write(f"{i}\t")
    f.write("\n")
f.close()
