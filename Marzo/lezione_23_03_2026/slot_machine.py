""" Slot machine """
import random

def spin():
    symbols = ["👽","❤️","😊","😎","🐈"]
    riga = []
    for x in range(3):
        riga.append(random.choice(symbols))
    return riga

def print_row(riga):
    print("*" * 20)
    print(" | ".join(riga))
    print("*" * 20)

def check(riga, puntata):
    if riga[0] == riga[1] == riga[2]:
        if riga[0] == "👽":
            return puntata * 2
        elif riga[0] == "❤️":
            return puntata * 3
        elif riga[0] == "😊":
            return puntata *1.5
        elif riga[0] == "🐈":
            return 1.2
        elif riga[0] == "😎":
            return puntata * 10
    return 0

def main():
    credits = 100
    
    print("-" * 30)
    print("Gioco puzzolente")
    print("-" * 30)
    
    while credits > 0:
        puntata = input("Hai a disposizione 100 crediti. Quanto vuoi puntare? (1-100) ")
        if not puntata.isdigit():
            print("Inserisci un valore numerico da 1 a 100 ")
            continue
    
        puntata = int(puntata) #casting, ovvero forzatura del tipo
        
        if puntata <= 0:
            print(f"La puntata deve essere maggiore di zero")
            continue
        
        if puntata > credits:
            print(f"Tu hai {credits} crediti, non puoi puntare {puntata} crediti")
            continue
        
        credits -= puntata
        
        riga = spin()
        
        print_row(riga)
        punteggio = check(riga, puntata)
        
        credits += punteggio
        print(f"I tuoi crediti sono {credits}")
        
        if credits == 0:
            print("GAME OVER")
            break
        
        play_again = input("Vuoi uscire? (Y/N) ").upper()
        if play_again == "Y":
            break
    
if __name__ == "__main__":
    main()