frutti = ["pere", "mele", "banane"]
verdure = ["broccoli", "spinaci", "barbabietole"]

frutti.insert(1, "arance")

if "melanzana" not in verdure:
    verdure.append("melanzane")

ortofrutticoli = [frutti, verdure]

# lettere = list("ciao")

# for lettera in lettere:
#     print(lettera, end = " - ")

# for frutto in frutti:
#     print(frutto)

frutti.append("fragole")

frutti.remove("fragole")

# clsfrutti.sort()

for prodotto in ortofrutticoli:
    print(prodotto)
print("*" * 30)

for prodotto in ortofrutticoli:
    for p in prodotto:
        print(p)
    print("-" * 10)