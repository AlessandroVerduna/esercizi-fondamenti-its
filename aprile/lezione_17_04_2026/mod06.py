import pandas as pd

df = pd.read_csv("auto.csv")

# print(df.dtypes)

# print(df.describe())

moto_sopra_10k = df[df["Prezzo (€)"] > 10000][["Marca", "Modello", "Prezzo (€)"]]
print(moto_sopra_10k)