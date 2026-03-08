"""
    Autore: Alessandro Verduna
    Data: 08/03/2026

    Titolo: Secondo esercizio (seconda parte)
        Si hanno in input N saldi di conti correnti bancari. Si vuole in output la media aritmetica dei
        soli conti correnti che hanno un saldo negativo
"""

# Viene richiesto tramite INPUT quanti conti correnti si vogliono inserire successivamente
# Si verifica che venga inserito un carattere accettato (es. no lettere)
def numero_conti_correnti(messaggio):
    while True:
        try:
            return int(input(messaggio))
        except ValueError:
            print("Solo numeri sono accettati!")

# Vengono inseriti i saldi dei conti corrente per un totale di volte prima definito
# Viene verificato che vengano inseriti valori validi (es. no lettere)
def inserimento_saldi(iterazioni, messaggio):
    lista = []
    for i in range(iterazioni):
        try:
            saldo = float(input(messaggio))
            lista.append(saldo)
        except ValueError:
            print("Solo valori numerici sono accettati")
    return lista

# Viene eseguita la media dei soli conti correnti con saldo negativo
# Nel caso in cui non siano stati inseriti saldi e la lista sia vuota viene stampato in messaggio che esplicita l'impossibilità
# di calcolare la media
def media(lista):
    if len(lista) == 0:
        print("Non hai inserito valori numerici. La media non può essere calcolata")
    else:
        somma = 0
        contatore = 0
        for i in lista:
            if i < 0:
                somma += i
                contatore += 1
        media = somma / contatore
        print(f"La media è {media}")
                
# Tutte le precedenti funzioni vengono concatenate
def main():
    print("\nInserisci un numero di saldi che vuoi inserire e successivamente\ninserisci i saldi uno a uno. Il programma ti calcolerà la media\nSOLO dei saldi negativi\n-----------------------------------------")
    iterazioni = numero_conti_correnti("Quanti saldi nuovi inserire? ")
    lista_saldi = inserimento_saldi(iterazioni, "Inserisci i saldi ")
    media(lista_saldi)
    print("esercizio terminato!")

# Esecuzione della funzione MAIN() che a cascata esegue le altre
if __name__ == "__main__":
    main()