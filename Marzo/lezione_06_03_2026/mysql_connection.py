import mysql.connector
import json

mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'its2026'
)

print("Connected to MySQL")

cursor = mycon.cursor()
query = 'select * from games;'
cursor.execute(query)

games = cursor.fetchall()

for game in games:
    print(game[1])

with open("games.json", "w", encoding = "utf-8") as f:
    json.dump(games, f, indent = 4)