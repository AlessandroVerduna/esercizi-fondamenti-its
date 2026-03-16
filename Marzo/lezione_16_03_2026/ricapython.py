""" Resume """

# frutta = ['mele', 'pere', 'banane']
# frutti_piccoli = ['mirtilli', 'lamponi']

# tutti_frutti = frutta + frutti_piccoli

# # print(type(frutta))
# # print(help(str))

# print(tutti_frutti)

# miao = tuple(('porco can '))
# bao = tuple(('bao'))

# print(type(miao))

# miaobao = miao + bao

# print(miaobao)

#           0       1         2
frutti = ['mele', 'pere', 'banane']

#               0           1           2
verdure = ['spinaci', 'costine', 'broccoli']


dolci = ['tiramisu', 'sorbetto', 'cannolo']

# for frutto in frutti:
#     print(frutto)

zippati = zip(frutti, verdure, dolci)

# print(frutti[0])
# print(frutti[1])
# print(frutti[2])

for a, b, c in zippati:
    print(a, b, c)
    
alimenti = frutti + verdure + dolci
print(alimenti)

scatola = [alimento for alimento in alimenti if alimento.startswith('canno')]

# for alimento in alimenti:
#     if alimento.startswith('c'):
#         scatola.append(alimento)

print(scatola)