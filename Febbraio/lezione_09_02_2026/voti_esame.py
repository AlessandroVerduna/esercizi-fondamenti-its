voti = [28, 25, 26, 24, 28, 29, 22, 30, 30, 18, 26, 21]

voti_top = []

for voto in voti:
    if voto >= 25:
        voti_top.append(voto)
        #print(voto)

          #[espressione ... ciclo for ... condizione]
voti_top = [voto for voto in voti if voto >= 25]

print(voti_top)

print(("Giammarco dammi la cazzo di sedia " * 3 + "\n") * 100)