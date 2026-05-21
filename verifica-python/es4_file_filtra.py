"""
ESERCIZIO 4

Uguale all'esercizio file precedente, ma:
file input: input.txt
file output deve chiamarsi: output_<nome>.txt
Esempio: output_Mauro.txt
Scrivere solo le righe che contengono i caratteri della stringa s in ordine
"""

# Input nome -> usato nel nome del file di output
nome = input("Inserisci il tuo nome: ")

# Stringa da cercare -> i caratteri devono apparire in ordine
s = input("Inserisci i caratteri che saranno cercati: ")

# Lettura del file di input
with open("input.txt", "r", encoding="utf-8") as file:
    contenuto = file.readlines()

    righe_filtrate = []

    # Controllo ogni riga del file
    for riga in contenuto:
        indice = 0  # posizione corrente nella stringa s

        # Scorro la riga carattere per carattere
        for lettera in riga:
            # Se la lettera corrisponde al carattere atteso -> passo al successivo
            if lettera == s[indice]:
                indice += 1

                # Se ho trovato tutti i caratteri di s -> la riga è valida
                if indice == len(s):
                    righe_filtrate.append(riga)
                    break

# Scrittura del file di output -> nome personalizzato
with open(f"output_{nome}.txt", "w", encoding="utf-8") as output:
    for riga in righe_filtrate:
        output.write(riga)