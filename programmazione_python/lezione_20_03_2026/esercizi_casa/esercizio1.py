"""
    Autore: Alessandro Verduna
    Data: 20/03/2026
    
    Consegna: Primo Esercizio
        Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
        restituisca espressa solamente in secondi. Successivamente creare un programma
        principale che chieda in input due quantità di tempo e stampi in output quale quantità di
        tempo è maggiore. La funzione deve avere i parametri formali con valori predefiniti.
"""

def return_time_in_seconds(ore, minuti, secondi):
    return ore * 3600 + minuti * 60 + secondi

def bigger_time_given(ora_a = 1, minuti_a = 40, secondi_a = 20, ora_b = 2, minuti_b = 50, secondi_b = 11):
    totale1 = return_time_in_seconds(ora_a, minuti_a, secondi_a)
    totale2 = return_time_in_seconds(ora_b, minuti_b, secondi_b)

    if totale1 > totale2:
        return "Il primo orario è maggiore"
    elif totale1 == totale2:
        return "I due orari sono uguali"
    else:
        return "Il secondo orario è maggiore"

def validation_input():
    while True:
        input_ore = int(input("Inserisci qui il numero di ore: "))
        input_minuti = int(input("Inserisci qui il numero di minuti: "))
        input_secondi = int(input("Inserisci qui il numero di secondi: "))
        
        if input_ore < 0:
            print("Valore di riferimento delle ore non valido")
        elif input_minuti < 0 or input_minuti > 59:
            print("Valore di riferimento dei minuti non valido")
        elif input_secondi < 0 or input_secondi > 59:
            print("Valore di riferimento dei secondi non valido")
        else:
            return input_ore, input_minuti, input_secondi 

def main():   
    a, b, c = validation_input()
    totale1 = return_time_in_seconds(a, b, c)        
    print(f"L'orario fornito equivale a: {totale1} secondi")

    risposta1 = input("Vuoi inserire un primo orario da comparare? (Y/N) ")
    risposta2 = input("Vuoi inserire un secondo orariod a comparare? (Y/N) ")

    if risposta1.capitalize() == "Y" and risposta2.capitalize() == "Y":
        a, b, c = validation_input()
        d, e, f = validation_input()
        print(bigger_time_given(a, b, c, d, e, f))
    elif risposta1.capitalize() == "Y" and risposta2.capitalize() != "Y":
        a, b, c = validation_input()
        print(bigger_time_given(a, b, c))
    elif risposta1.capitalize() != "Y" and risposta2.capitalize() == "Y":
        d, e, f = validation_input()
        print(bigger_time_given(ora_b = d, minuti_b = e, secondi_b = f))
    else:
        print(bigger_time_given())

if __name__ == "__main__":
    main()