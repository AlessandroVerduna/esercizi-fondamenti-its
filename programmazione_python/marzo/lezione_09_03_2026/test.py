# a = 1
# print("id prima modifica: ", id(a))
# a += 1
# print("id dopo modifica: ", id(a))

# a = [1,2]
# print("id prima modifica:", id(a))
# a += [3]
# print("Id dopo modifia:", id(a))

# def fun(a):
#     #a += 1
#     print(id(a))

# a = 1
# print(id(a))
# fun(a)

# def fun(a):
#     print("id(a) prima modifica:", id(a))
#     a += 1
#     print("id(a) dopo modifica:", id(a))
#     print("Valore a dopo modifica:", a)

# a = 1
# print("id(a) prima chiamata:", id(a))
# fun(a)
# print("id(a) dopo chiamata:", id(a))
# print("Valore a dopo funzione:", a)

# def areaRettangolo(base = 2, altezza = 4):
#     return base * altezza

# print("Area 1 = ", areaRettangolo())
# print("Area 2 = ", areaRettangolo(5))
# print("Area 3 = ", areaRettangolo(5, 5))

# def areaRettangolo(base, altezza, profondita):
#     return base * altezza * profondita

# print("Area 1 = ", areaRettangolo(3, profondita=4, altezza=5))
# print("Area 2 = ", areaRettangolo(profondita=4, altezza=5, base=3))

# def fun(a, b):
#     somma = a + b
#     print("Somma = ", somma)
#     return somma

# print(fun(2, 3))
# print("Somma = ", somma)

# var = 10
# def fun():
#     print("2 var = ", var)
#     var = var + 1
#     print("3 var = ", var)

# print("1 var = ", var)
# fun()
# print("4 var = ", var)

print("Stampa su prima riga", end="\n")
print("Stampa su seconda riga")
print("Stampa su terza riga", end="\t")
print("dopo tab su terza riga ", end=" XXX ")
print("ancora su terza riga ")
print("Fine esempio su quarta riga ")

valore = 10
print(f"Valore: {valore}")
print(f"Valore con 3 cifre (valore:03)")
print(f"Valore con 3 'posizioni' {valore:3}")
numero = 10.456
print(f"Numero con 2 cifre decimali {numero:.2f}")
print(f"Numero con 10 cifre decimali {numero:.10f}")
print(f"Numero: {numero:e}")
print(f"Numero: {numero:.3e}")

str1 = 'a'
num2 = 15
str3 = 'abc'
str4 = 'abcd'
print(f'{str1:>10}')
print(f'{num2:>10}')
print(f'{str3:<10}')
print(f'{str4:>10}')
