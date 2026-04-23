var = 10
def somma():
    global var
    print("Var 2 = ", var)
    var = var + 1
    print("Var 3 = ", var)

print("Var 1 = ", var)
somma()
print("Var 4 = ", var)
