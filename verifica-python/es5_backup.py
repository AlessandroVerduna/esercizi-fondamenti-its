"""
ESERCIZIO 5

scrivere un programma che simula un tool di backup.
Input:
nome studente
lista di file (nomi file come stringhe, uno per riga)
la lista termina quando l'utente inserisce "STOP"
Regole:
se un file termina con .tmp o .log non va salvato (ignorato)
gli altri vanno aggiunti al backup
Output finale:
Backup Report - <nome>
File inclusi: X
File esclusi: Y
Elenco inclusi:
- ...
- ...
"""

# Input nome -> usato nel report finale
nome = input("Inserisci il tuo nome: ")

# Variabili di controllo
verificatore = True
lista_file = []
contatore_esclusi = 0
contatore_inclusi = 0

# Raccolta file fino a STOP
while verificatore == True:
    file = input("Inserisci un file da aggiungere al backup (inserisci 'stop' o 'STOP' per finire l'inserimento): ")

    # STOP -> termina la raccolta
    if file.upper() == "STOP":
        verificatore = False

    # File da escludere -> .tmp o .log
    elif file.endswith(".tmp") or file.endswith(".log"):
        contatore_esclusi += 1

    # File valido -> aggiunto al backup
    else:
        contatore_inclusi += 1
        lista_file.append(file)

# Report finale
print(f"""
Backup Report - {nome}
File inclusi: {contatore_inclusi}
File esclusi: {contatore_esclusi}
Elenco inclusi:""")

# Stampa elenco file inclusi
for elemento in lista_file:
    print(f"- {elemento}")