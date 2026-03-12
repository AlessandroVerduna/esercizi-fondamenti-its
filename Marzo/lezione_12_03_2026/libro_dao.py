import mysql.connector
from libro import Libro

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'biblioteca'
)

cursor = db.cursor()

cursor.execute("select * from libri;")

libri = cursor.fetchall()

print("Connected to MySQL")

tabella_libri = []

for libro in libri:
    libroId = libro[0]
    collocazione = libro[1]
    autore = libro[2]
    titolo = libro[3]
    editore = libro[4]
    classificazione = libro[8]
    
    libro = Libro(libroId, collocazione, autore, titolo, editore, classificazione)
    tabella_libri.append(libro)
    
    #print(libro)