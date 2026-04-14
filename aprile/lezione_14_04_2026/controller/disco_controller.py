from service.disco_service import DiscoService
from model.artist import Artist
from model.album import Album

class DiscoController:
    def getArtists(self):
        service = DiscoService()
        artisti = service.getAllArtists()
        output = []

        for artista in artisti:
            temp = Artist(artista.get("ArtistId", 0), artista.get("Name", 'Artista sconosciuto'))
            output.append(temp.toTuple())
        return output
    
    def getArtistiJson(self):
        service = DiscoService()
        return service.getAllArtists()    
    


# artisti = [{
#     "ArtistId": 1,
#     "Name": "AC/DC"
# },
# {
#     "ArtistId": 3,
#     "Name": "Aerosmith"
# }           
# ]

# a1 = Artist(artisti[0].get("ArtistId", 0), artisti[0].get("Name", 'Artista sconosciuto'))
# a2 = Artist(artisti[1].get("ArtistiId", 0), artisti[1].get("Name", 'Artista sconosciuto'))
# # print(a1)

# # print(isinstance(a1, Album))
# # print(isinstance(a1, Artist))

# print(a1.nome)
# print(a1.casa_discografica)

# print(a2.nome)
# print(a2.casa_discografica)