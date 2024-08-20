while True:
    entry = int(input())
    if entry == 0:
        break
    numbers = []
    for i in range(entry):
        num = i + 1
        values = []
        for j in range(entry):
            values.append(abs(num))
            if num == 1:
                num -= 3
            else:
                num -= 1
        numbers.append(values)
        
    for i in range(len(numbers)):
        tx = ''
        for j in range(len(numbers)):
            tx += " %3d" %numbers[i][j]
        print(tx[1:])
    print("")