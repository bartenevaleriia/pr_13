n = int(input('Введите n '))
symbols = []
for i in range(n):
    string = input('Введите символ ')

    for symbol in string:
        symbols.append(symbol)

print(symbols)