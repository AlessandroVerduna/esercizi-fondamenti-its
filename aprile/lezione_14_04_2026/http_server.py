from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Chinook"
)

@app.route("/studenti")
def studenti():
    studente = { "nome": "pippo", "eta": 25, "data_nascita": '2000-04-13' }
    return studente

@app.route("/artists")
def artist():
    cursore = db.cursor(dictionary=True)
    cursore.execute("SELECT * FROM artist;")
    artisti = cursore.fetchall()
    return artisti

@app.route("/album")
def album():
    cursore = db.cursor(dictionary=True)
    cursore.execute("select ar.name, a.title from album a join artist ar using (ArtistId);")
    album = cursore.fetchall()
    return jsonify(album)

app.run(debug = True, port = 5000)