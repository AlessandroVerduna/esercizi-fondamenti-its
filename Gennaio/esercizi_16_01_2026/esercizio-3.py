eta = int(input("Qual'è la tua età? "))
accompagnamento = str(input("Sei accompagnato? [Sì/No] "))

if eta >= 16 or accompagnamento == "Sì":
    print("Puoi entrare")
else:
    print("Non puoi entrare")