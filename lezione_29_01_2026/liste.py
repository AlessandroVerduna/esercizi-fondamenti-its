frutta = ['pere', 'mele', 'fragole']
verdura = list(['spinaci', 'barbabietole', 'broccoli'])

frutta.append("banane")
verdura.append("carote")

prodotti_orto = list(frutta + verdura)

print(type(prodotti_orto))

for prodotti in prodotti_orto:
    print(f"Prodotto : {prodotti} ------- peso : {0.5 + 0.5}kg")