piemonte = ['Asti', 'Cunero', 'Torino', 'Alessandria']

liguria = ['Savona', 'Genova', 'La Spezia', 'Imperia']

piemonte.extend(['Biella', 'Novara'])
liguria.append(['Biella', 'Novara'])

piemonte.sort()

print(piemonte)
print(liguria)

if 'Torino' in piemonte:
    print("Torino c'é")

citta = input("Dimmi la citta dove vuoi andare: ")

if citta in piemonte:
    print(f"Il bus per {citta} è disponibile")
else:
    print(f"il bus per {citta} non è disponibile")