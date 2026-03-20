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
    if ora_a > ora_b:
        return "Il primo orario fornito è più grande"
    elif ora_b > ora_a:
        return "Il secondo orario fornito è più grande"
    elif minuti_a > minuti_b:
        return "Il primo orario fornito è più grande"
    elif minuti_b > minuti_a:
        return "Il secondo orario fornito è più grande"
    elif secondi_a > secondi_b:
        return "Il primo orario fornito è più grande"
    elif secondi_b > secondi_a:
        return "Il secondo orario fornito è più grande"
    else:
        return "I due orari sono uguali!"

def validation_input():
    verificatore = False
    while verificatore == False:
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
            verificatore = True
    return input_ore, input_minuti, input_secondi 

def main():   
    # verificatore = False
    # while verificatore == False:
    #     input_ore = int(input("Inserisci qui il numero di ore: "))
    #     input_minuti = int(input("Inserisci qui il numero di minuti: "))
    #     input_secondi = int(input("Inserisci qui il numero di secondi: "))
        
    #     if input_ore < 0:
    #         print("Valore di riferimento delle ore non valido")
    #     elif input_minuti < 0 or input_minuti > 59:
    #         print("Valore di riferimento dei minuti non valido")
    #     elif input_secondi < 0 or input_secondi > 59:
    #         print("Valore di riferimento dei secondi non valido")
    #     else:
    #         verificatore = True
    a, b, c = map(int, validation_input())        
    print(f"L'orario fornito equivale a: {return_time_in_seconds(a, b, c)} secondi")

    print(bigger_time_given())

if __name__ == "__main__":
    main()