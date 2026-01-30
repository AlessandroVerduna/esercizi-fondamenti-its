magazzino = [
    ['Maglia Bucata', 100], 
    ['Maglia Verde', 70], 
    ['Maglia Rossa', 90]
]

f = open('magazzino.html', 'w')

f.write('<html>\n')
f.write('<head>\n')
f.write('</head>\n')
f.write('<body>\n')

f.write('<h1> Magazzino prodotti</h1>\n')

f.write('<ul>\n')

for prodotto in magazzino:
    nome = prodotto[0]
    quantita = prodotto[1]
    
    f.write(f"<li>{nome}: {quantita}</li>")



f.write('</ul>\n')

f.write('</body>')
f.write('</html>\n')

f.close()

print("Elaborazione terminata")

