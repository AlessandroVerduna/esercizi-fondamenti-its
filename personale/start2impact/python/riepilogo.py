def verifica_palindromo(parola):
    if parola == parola[::-1]:
        return "La parola è palindroma"
    else:
        return "La parola non è palindroma"

def main():
    parola = input("Inserisci una parola e verificherò se è palindroma: ")
    verifica = verifica_palindromo(parola)
    print(verifica)

if __name__ == "__main__":
    main()