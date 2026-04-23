x = 1
y = 10
print(f"{x} e {y}")
print(type(x))
print(type(y))

x, y = y, x
print(f"{x} e {y}")
print(type(x))
print(type(y))