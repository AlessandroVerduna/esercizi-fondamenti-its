import random as rnd

nome = ["alessandro","giorgio"]
aggettivo1 = ["rosso","bianco"]
animale = ["gatto","cane"]
cibo = ["pizza","pasta"]
numero = ["9","2"]
colore = ["rosso","bianco"]
verbo = ["mangire","bere"]

with open("stories.txt", "w") as f:
    for x in range(10):

        f.write(f"---------------------------------storia {x + 1}------------------------------")

        storia = f"""
        LA STORIA DI {rnd.choice(nome).upper()} 

        C'era una volta {rnd.choice(nome)}, una persona molto {rnd.choice(aggettivo1)}.
        Un giorno, mentre camminava nel bosco, incontrò un {rnd.choice(animale)} {rnd.choice(colore)}.
        L'animale aveva {rnd.choice(numero)} pezzi di {rnd.choice(cibo)} e voleva {rnd.choice(verbo)}.
        {rnd.choice(nome)} decise di aiutarlo e insieme vissero felici e contenti!
        """

        f.write(storia)