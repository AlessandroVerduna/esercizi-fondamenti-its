prezzo = float(input("Qual'è il prezzo del prodotto? "))

stato = "stock"

if prezzo < 10 and stato == "stock":
     print("Lo sconto è applicabile")
else:
   print("Lo sconto non è applicabile")

# prezzo = int(8)
# stato = "stock"

# if prezzo < 10 and stato == "stock":
#     print("Il prodotto accede allo sconto")
# else:
#     print("Il prodotto non accede allo sconto")

