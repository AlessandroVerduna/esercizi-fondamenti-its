# import requests
# import time

# url = "http://localhost:3000/api/v1"

# while True:
#     response = requests.get(url + '/catalogo')
#     data = response.json()

#     print("Dati ricevuti!")
    
#     time.sleep(5)

import requests
import json
import time

URL = "http://localhost:3000/api/v1/catalogo"

def aggiorna_catalogo():
    response = requests.get(URL)
    data = response.json()

    with open("catalogo.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("catalogo.json aggiornato!")

while True:
    aggiorna_catalogo()
    time.sleep(5)
