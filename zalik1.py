file = open("forzalik.txt", "r")
words = 0
symbol = 0
number = 0
for i in file:
    number += 1
    for a in i:
        if a not in (" ", '\n', '\t'):
            symbol += 1

    pos = 'out'
    for a in i:
        if a != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif a == ' ':
            pos = 'out'
    print("У рядку номер -", number, "кількість слів -", words, "кількість символів -", symbol)
    symbol = 0
    words = 0
