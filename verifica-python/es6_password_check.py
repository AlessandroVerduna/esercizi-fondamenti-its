"""
ESERCIZIO 6

Chiedere:
nome studente
password
La password è valida se:
almeno 8 caratteri
contiene almeno una lettera maiuscola
contiene almeno una minuscola
contiene almeno un numero
Stampare:
<nome> - Password valida oppure <nome> - Password non valida
"""

# Input nome
nome = input("Inserire nome studente: ")

# Input password -> da validare
password = input("Inserire password per validazione: ")

# Controlli richiesti dal testo
lunghezza_ok = len(password) >= 8
maiuscola_ok = any(car.isupper() for car in password)
minuscola_ok = any(car.islower() for car in password)
numero_ok = any(car.isdigit() for car in password)

# Validazione finale -> tutte le condizioni devono essere vere
if lunghezza_ok and maiuscola_ok and minuscola_ok and numero_ok:
    print(f"{nome} - Password valida")
else:
    print(f"{nome} - Password non valida")