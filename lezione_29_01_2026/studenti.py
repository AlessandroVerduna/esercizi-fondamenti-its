studenti = []

f = open("studenti.txt")

for riga in f:
    #print(riga)
    riga = riga.replace("\n", "")
    riga = riga.replace("\t", ",")
    studenti.append(riga)

f.close()

f = open('studenti.sql', 'w')

query_tabella = """
DROP TABLE IF EXISTS studenti;\n\n
CREATE TABLE studenti(\n
    id int primary key auto_increment,\n
    nome varchar(30) not null,\n
    cognome varchar(50) not null\n
);\n\n
"""

f.write(query_tabella)

for studente in studenti:
    pezzi = studente.split(",")
    nome = pezzi[0]
    cognome = pezzi[1]
    #print(f"Il nome dello studente è {nome} e il cognome è {cognome}")
    f.write(f"insert into studenti (nome, cognome) value ('{nome}', '{cognome}');\n")
f.close()