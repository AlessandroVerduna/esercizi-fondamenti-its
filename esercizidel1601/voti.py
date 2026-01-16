voti = [28,25,26,29,30]

totale = 0

quantity = len(voti)
#print(quantity)

for voto in voti:
    #print(voto)
    totale = totale + voto
print(f"Il totale dei voti è {totale}: ")

media = totale / quantity
print(media)