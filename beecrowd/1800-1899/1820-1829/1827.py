import math

def diag(i, j, num, value):
    if i == j:
        return value
    return num

while True:
    try:
        entry = int(input())
        numbers = [[0] * entry] * entry

        numbers = [[diag(i, j, numbers[i][j], 3) for j in range(entry)] for i in range(entry)]
        for i in range(entry):
            numbers[i].reverse()
        numbers = [[diag(i, j, numbers[i][j], 2) for j in range(entry)] for i in range(entry)]

        count = 0
        nSquares = entry - 4
        values = [1, 3, 5]
        if not nSquares in values:
            n = 6
            while True:
                nSquares -= n
                count += 1
                if nSquares in values:
                    break
                
        center = entry // 2
        start = center - count - 1
        end = center + count + 1

        for i in range(start, end + 1):
            for j in range(start, end + 1):
                numbers[i][j] = 1
        numbers[center][center] = 4
        for i in range(entry):
            numbers[i] = list(map(str, numbers[i]))
            print("".join(numbers[i]))
        print()
    except EOFError:
        break