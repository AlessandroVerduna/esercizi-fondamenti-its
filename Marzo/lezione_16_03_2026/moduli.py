import requests

# url = 'https://pokeapi.co/api/v2/pokemon/'

# risposta = requests.get(url + 'buizel')

# if risposta.status_code == 200:
#     pokemon = risposta.json()
    
#     for chiave, valore in pokemon.items():
#         print(f"La chiave {chiave}, e il valore {valore}")
#         print('\n\n\n')
        
url = 'https://api.tvmaze.com/singlesearch/shows?q='

cerca = input("Cosa vuoi cercare ? ")

risposta = requests.get(url + cerca)

if risposta.status_code == 200:
    show = risposta.json()
    
    titolo = show.get('name')
    rating = show.get('rating')
    image = show.get('image')
    
    print(titolo, rating['average'], image['medium'])