""" Gestione di richieste http """

import requests
from film import Film

URL = "https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/imdb_top_2000_movies.json"

request = requests.get(URL)
if request.status_code == 200:
    oggetto_pitonico = request.json()
    for movie in oggetto_pitonico:
        title = movie["Movie Name"]
        director = movie["Director"]
        year = movie["Release Year"]
        rating = movie["IMDB Rating"]
        f = Film(title, director, year, rating)
        print(f)            