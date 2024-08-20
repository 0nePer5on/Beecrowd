while True:
    entry = int(input())
    if entry == 0:
        break
    numbers = []
    for i in range(entry):
        values = []
        for j in range(0, entry):
            values.append(2 ** (j + i))
        numbers.append(values)
   
    numbers = [list(map(str, numbers[i])) for i in range(entry)]
    length = len(numbers[entry - 1][entry - 1])

    for i in range(entry):
        for j in range(entry):
            while len(numbers[i][j]) < length:
                numbers[i][j] = ' ' + numbers[i][j]
        txt = ' '.join(numbers[i])
        print(txt)
    print()