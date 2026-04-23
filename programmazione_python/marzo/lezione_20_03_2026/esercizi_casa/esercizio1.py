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
    """
    Calcola il corrispondente in secondi del formato ore, minuti, secondo passato per parametri.
    Parametri:
        ore (int): numero di ore
        minuti (int): numero di minuti
        secondi (int): numero di secondi
    Ritorna:
        Ritorna un 'int' che corrisponde all'ammontare in secondi dell'orario fornito
    """
    return ore * 3600 + minuti * 60 + secondi

def bigger_time_given(ora_a = 1, minuti_a = 40, secondi_a = 20, ora_b = 2, minuti_b = 50, secondi_b = 11):
    """
    Esegue dei confronti tra due orari forniti per verificare quale sia il maggiore.
    Parametri:
        ora_a, ora_b (int): numero di ore del primo e secondo orario
        minuti_a, minuti_b (int): numero di minuti del primo e secondo orario
        secondi_a, secondi_b (int): numero di secondi del primo e secondo orario
    Ritorna:
        Una stringa in cui viene indicato qual'è l'orario più grande tra quelli forniti
    """
    totale1 = return_time_in_seconds(ora_a, minuti_a, secondi_a)
    totale2 = return_time_in_seconds(ora_b, minuti_b, secondi_b)

    if totale1 > totale2:
        return "Il primo orario è maggiore"
    elif totale1 == totale2:
        return "I due orari sono uguali"
    else:
        return "Il secondo orario è maggiore"

def input_and_validation():
    """
    Consente di inserire l'input in formato ore, minuti, secondi verificando anche la validità dei dati inseriti
    e li richiede all'utente qual'ora fossero errati.
    Parametri:
        NONE
    Ritorna:
        input_ore (int): dato validato corrispondente al numero di ore
        input_minuti (int:): dato validato corrispondente al numero di minuti
        input_secondi (int): dato validato corrispondente al numero di secondi
    """
    correttezza_input = False
    while correttezza_input != True:
        input_ore = input("Inserisci qui il numero di ore: ")
        input_minuti = input("Inserisci qui il numero di minuti: ")
        input_secondi = input("Inserisci qui il numero di secondi: ")
        
        #if (input_ore is int) and (input_minuti is int) and (input_secondi is int):
        if input_ore.isdigit() and input_minuti.isdigit() and input_secondi.isdigit():
            input_ore = int(input_ore)
            input_minuti = int(input_minuti)
            input_secondi = int(input_secondi)
            if input_ore < 0:
                print("Valore di riferimento delle ore non valido")
            elif input_minuti < 0 or input_minuti > 59:
                print("Valore di riferimento dei minuti non valido")
            elif input_secondi < 0 or input_secondi > 59:
                print("Valore di riferimento dei secondi non valido")
            else:
                correttezza_input = True
        else:
            print("Valore numero inserito in formato non valido. Inserire solo interi")
    return input_ore, input_minuti, input_secondi 

def main():   
    """
    Funzione principale del programma.
    Chiede gli input e li verifica tramite input_and_validation(). Attraverso return_time_in_seconds() ottiene il corrispettivo
    in secondi dell'orario inserito e lo stampa nel terminale.

    Chiede se si vogliono inserire altri due orari che saranno comparati al fine di identificare quello più grande
    attraverso la funzione bigger_time_given()
    """
    a, b, c = input_and_validation()
    totale1 = return_time_in_seconds(a, b, c)        
    print(f"L'orario fornito equivale a: {totale1} secondi")

    risposta1 = input("Vuoi inserire un primo orario da comparare? (Y/N) ")
    risposta2 = input("Vuoi inserire un secondo orariod a comparare? (Y/N) ")

    if risposta1.capitalize() == "Y" and risposta2.capitalize() == "Y":
        a, b, c = input_and_validation()
        d, e, f = input_and_validation()
        print(bigger_time_given(a, b, c, d, e, f))
    elif risposta1.capitalize() == "Y" and risposta2.capitalize() != "Y":
        a, b, c = input_and_validation()
        print(bigger_time_given(a, b, c))
    elif risposta1.capitalize() != "Y" and risposta2.capitalize() == "Y":
        d, e, f = input_and_validation()
        print(bigger_time_given(ora_b = d, minuti_b = e, secondi_b = f))
    else:
        print(bigger_time_given())

if __name__ == "__main__":
    main()