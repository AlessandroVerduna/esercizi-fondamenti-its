
# if __name__ == '__main__':
#     print(__name__)
# else:
#     print('Proco can sono modulo 1')

frutti = ['mele', 'pere', 'banane']

def addizione(a: int, b: int):
    return a + b

def main():
    print("Sono il metodo main del modulo 1")
    print(addizione(4,5))
    
if __name__ == '__main__':
    main()