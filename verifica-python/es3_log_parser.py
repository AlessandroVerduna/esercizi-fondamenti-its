"""
ESERCIZIO 3

Il programma deve calcolare e stampare:
    1. numero totale richieste
    2. numero richieste con status 200
    3. numero richieste con status 404
    4. IP che ha fatto più richieste
    5. tempo medio di risposta (media di CODE_MS)
"""

# Lettura file log -> ogni riga contiene data, ora, IP, metodo, URL, status, ms
with open("access_log.txt", "r", encoding="utf-8") as f:
    righe = f.readlines()

# Input nome
nome = input("Inserisci nome dello studente: ")

# Variabili di conteggio
totale = 0
status_lista = []
ip_count = {}
tempi = []

# Parsing di ogni riga del log -> estrazione campi utili
for riga in righe:
    parti = riga.strip().split()

    ip = parti[2]
    status = int(parti[5])
    tempo = int(parti[6])

    totale += 1
    tempi.append(tempo)
    status_lista.append(status)

    # Conteggio richieste per IP
    if ip not in ip_count:
        ip_count[ip] = 0
    ip_count[ip] += 1

# IP con più richieste -> max su dizionario
ip_attivo = max(ip_count, key=ip_count.get)

# Media dei tempi di risposta
media_tempo = sum(tempi) / len(tempi)

# Conteggi status specifici
status_200 = status_lista.count(200)
status_404 = status_lista.count(404)

# Output finale richiesto
print(f"""
Report log - Studente: {nome}
  Totale richieste: {totale}
  Status 200: {status_200}
  Status 404: {status_404}
  IP più attivo: {ip_attivo}
  Tempo medio risposta: {media_tempo:.2f} ms
""")
