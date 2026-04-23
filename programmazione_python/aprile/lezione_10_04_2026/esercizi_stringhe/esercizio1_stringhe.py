"""
    Autore: Alessandro Verduna
    Data: 10/04/2026

    Consegna: Primo Esercizio
        Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota.
        Progettare una funzione che accetti la stringa, la posizione del carattere e restituisca la
        stringa modificata.
"""

def stringa_input_validata():
    """
    
    """
    stringa = input("Inserisci una stringa: ")
    if len(stringa) != 0:
        return stringa

def input_validazione_posizione_carattere():
    """
    
    """
    posizione_carattere = int(input("Indica la posizione: "))
    return posizione_carattere

def realizzazione_output():
    """
    
    """
    stringa_output = ""
    for i in range(len(input_stringa_validato)):
        if input_stringa_validato[i] != input_stringa_validato[input_posizione_carattere_validato]:
            stringa_output += input_stringa_validato[i]
    return stringa_output

def main():
    """
    
    """
    global input_stringa_validato
    global input_posizione_carattere_validato

    input_stringa_validato = stringa_input_validata()
    input_posizione_carattere_validato = input_validazione_posizione_carattere()
    stringa_output = realizzazione_output()
    print(stringa_output)

if __name__ == "__main__":
    main()