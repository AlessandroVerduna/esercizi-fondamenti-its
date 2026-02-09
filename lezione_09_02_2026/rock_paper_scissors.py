import random

mossa = ['rock', 'paper', 'scissors']

macchina = random.choice(mossa)

umano = input("Umano! Scegli tra: rock, scissors, paper||| ")

print(f"La macchina ha scelto {macchina} e l'umano ha scelto {umano}")

if macchina == umano:
    print("Pari!")
elif macchina == "paper" and umano == "rock":
    print("Vince la macchina")
elif macchina == "rock" and umano == "scissors":
    print("Vince la macchina")
elif macchina == "scissors" and umano == "paper":
    print("Vince la macchina")
else:
    print("L'umano vince")


