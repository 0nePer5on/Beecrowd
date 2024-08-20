def diag(i, j, num, value):
    if i == j:
        return value
    return num

while True:
    try:
        entry = int(input())
        numbers = [[3] * entry] * entry
        numbers = [[diag(i, j, numbers[i][j], 1) for j in range(entry)] for i in range(entry)]
        for i in range(entry):
            numbers[i].reverse()
        numbers = [[diag(i, j, numbers[i][j], 2) for j in range(entry)] for i in range(entry)]
        for i in range(entry):
            numbers[i].reverse()
        for i in range(entry):
            value = numbers[i]
            value = list(map(str, value))
            print("".join(value))
    except EOFError:
        break