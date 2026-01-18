# sensore = True

# movimento = True

sensore = input("Il sensore è attivo? (True/False): ")
if sensore == "True":
    sensore = True
else:
    sensore = False

movimento = input("E' stato rilevato un movimento? (True/False): ")
if movimento == "True":
    movimento = True
else:
    movimento = False

if sensore == True and movimento == True:
    print("Warning! Movimento rilevato!")
elif sensore == True and movimento == False:
    print("Nessun movimento rilevato")
elif sensore == False:
    print("Sensore disattivato! Prestare attenzione!")