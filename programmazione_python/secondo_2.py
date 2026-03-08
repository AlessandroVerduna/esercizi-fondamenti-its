"""
    Autore: Alessandro Verduna
    Data: 08/03/2026

    Titolo: Secondo esercizio (seconda parte)
        Si hanno in input N saldi di conti correnti bancari. Si vuole in output la media aritmetica dei
        soli conti correnti che hanno un saldo negativo
"""

def numero_conti_correnti(messaggio):
    while True:
        try:
            return int(input(messaggio))
        except ValueError:
            print("Solo numeri sono accettati!")

def inserimento_saldi(iterazioni, messaggio):
    lista = []
    for i in range(iterazioni):
        try:
            saldo = float(input(messaggio))
            lista.append(saldo)
        except ValueError:
            print("Solo valori numerici sono accettati")
    return lista

def media(lista):
    if lista.lenght() == 0:
        print("MIAO")
    else:
        somma = 0
        contatore = 0
        for i in lista:
            if i < 0:
                somma += i
                contatore += 1
        media = somma / contatore
        print(f"La media è {media}")
            
        

def main():
    iterazioni = numero_conti_correnti("Quanti saldi nuovi inserire? ")
    lista_saldi = inserimento_saldi(iterazioni, "Inserisci i saldi ")
    media(lista_saldi)
    print("esercizio terminato!")

if __name__ == "__main__":
    main()