""" Applicativo per processare file JSON """

import json

istruzioni_insert = []

# Prendo i dati, li trasformo e li collezziono
with open("games.json", "r", encoding = "utf-8") as f:
    games = json.load(f)
    for game in games:
        nome = str(game.get("Game", "Nome gioco")).replace("'", "\\'")
        genere = str(game.get("Genre", "Genere")).replace("'", "\\'")
        publisher = str(game.get("Publisher", "Publisher")).replace("'", "\\'")
        platform = str(game.get("Original platform(s)[a]")).replace("'", "\\'")
        year = game.get("year", 0)
        year = int(year)

        istruzioni_insert.append(f"insert into games (nome, genere, publisher, platform, year) values ('{nome}', '{genere}', '{publisher}', '{platform}', {year});")

# Preparo un file SQL per inserire i dati sul database
query_tabella = """
use its2026;

drop table if exists games;

create table games(
    game_id int primary key auto_increment,
    nome varchar(100),
    genere varchar(100),
    publisher varchar(100),
    platform varchar(100),
    year int check (year > 1960)
);

"""

with open("games.sql", "w", encoding = "utf-8") as f:
    f.write(query_tabella)

    for istruzione in istruzioni_insert:
        f.write(istruzione)
        f.write("\n")
print("eleborazione conclusa")