""" Lancia dadi """

import random
import time

#print(random.random())

num_lanci = 10_000_000
vittorie = 0

start = time.time()
for i in range(num_lanci):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    if dado_1 == dado_2:
        #print(f"Hai vinto con una coppia di {dado_1}")
        vittorie += 1
    # print(f"Il valore di dao 1 è: {dado_1}")
    # print(f"Il valore di dao 2 è: {dado_2}")
    #print("----------------------------------------------")
stop = time.time()

print(f"Hai lanciato {num_lanci} volte e hai vinto {vittorie} volte")
print(f"La percentuale di vittorie è del {vittorie / float(num_lanci) * 100}%")
print(f"L'elaborazione è durata {stop - start:.2f} secondi")