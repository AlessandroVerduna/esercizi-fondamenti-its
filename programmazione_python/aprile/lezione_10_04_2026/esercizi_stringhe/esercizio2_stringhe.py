"""
    Autore: Alessandro Verduna
    Data: 10/04/2026

    Consegna: Secondo Esercizio
        Scrivere un programma che dica se una stringa è palindroma.
        Esempio:
        str="ABBA" PALINDROMA
        str="PIPPO" NON PALINDROMA
"""
def input_and_validazione_stringa():
    """
    
    """
    validatore = False
    stringa_input = input("Inserisci una stringa e verificherò che sia palindroma: ")
    while validatore == False:
        if len(stringa_input) < 2:
            print("Inserire una stringa composta da almeno due caratteri")
            stringa_input = input("Inserisci una stringa e verificherò che sia palindroma: ")
        else:
            stringa_input = stringa_input.lower()
            validatore = True
    return stringa_input

def verifica_palindromo(stringa):
    """
    
    """
    if stringa == stringa[::-1]:
        return True
    else:
        return False

def main():
    """
    
    """
    stringa = input_and_validazione_stringa()
    risultato = verifica_palindromo(stringa)

    if risultato:
        print("E' palindromo")
    else:
        print("Non è palindromo")

if __name__ == "__main__":
    main()