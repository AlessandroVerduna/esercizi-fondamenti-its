import json

from mod04 import leggi_file_csv

moto = leggi_file_csv("moto.csv")

with open("moto.json", "w") as f:
    json.dump(moto, f, indent=4)