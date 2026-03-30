import mysql.connector
from dataclasses import dataclass

@dataclass
class Prodotto:
    nome: str
    prezzo: float
    giacenza: int

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "magazzino"
)

cursore = db.cursor()

query = "select nome, prezzo_unitario, quantita_stock from prodotti;"

cursore.execute(query)

risultati = cursore.fetchall()

tendina = [Prodotto(nome = n, prezzo = p,giacenza =  q) for n, p, q in risultati]

print(tendina)

with open("Esercizio_magazzino.txt", "w") as f:
    f.write(f"{query}\n\n")
    
    # for row in tendina:
    #     f.write(f"{row[0]:30} {row[1]:10} {row[2]:5}\n")
    
    for p in tendina:
        f.write(f"{p.nome:30} {p.prezzo:10} {p.giacenza:5}\n")