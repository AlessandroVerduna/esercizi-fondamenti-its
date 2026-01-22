citta = ["Milano", "Torino", "Nice"]

def checkTemperatura(citta):
    frase = f"Qual'è la temeperatura esterna della città di {citta}? "
    temperatura = int(input(frase))
    if temperatura > 25:
        print("Fa caldo")
        print("Accendi il ventilatore")
    elif temperatura > 15:
        print("Come si sta bene oggi")
        print("Spegni il ventialtore")
    else:
        print("Oggi fa freddo")
        print("Accendi il riscaldamento")

for c in citta:
    print(c)
    checkTemperatura(c)

print("Bye")