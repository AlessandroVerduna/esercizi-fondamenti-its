import os

#os.chdir('../')

# Informazioni directory
# print(f"Directory corrente: {os.getcwd()}")
# print(f"Contenuto directory: {os.listdir('.')}")

# for elem in os.listdir('.'):
#     print(elem)

# os.mkdir("fatta_in_fad")
# os.mkdir("fatta_in_fad")

studenti_file = open("studenti.txt", "r", encoding="utf-8", newline='\n')
lettura = studenti_file.read()
for riga in lettura.splitlines():
    os.mkdir(riga)
studenti_file.close()