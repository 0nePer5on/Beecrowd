from operator import itemgetter

count = 1
while True:
    num = int(input())
    if num == 0:
        break
    numbers, results = list(), list()
    total = [0, 0]
    for n in range(num):
        values = input().split()
        values = [eval(i) for i in values]
        numbers.append(values)
        numbers[n].append(int(numbers[n][1] / numbers[n][0]))
        total[0], total[1] = total[0] + numbers[n][0], total[1] + numbers[n][1]
    sorted(numbers, key=itemgetter(2))
    numLen = len(numbers)
    i = 0
    while True:
        if i + 1 == numLen:
            break
        if numbers[i][2] == numbers[i + 1][2]:
            numbers[i][0] += numbers[i + 1][0]
            numLen -= 1
            numbers.pop(i + 1)
            i = 0
        else:
            i += 1
    
    text = ''
    for i in range(numLen):
        if i + 1 == range(numLen):
            text = text + str(numbers[i][0]) + '-' + str(numbers[i][2])
            break
        text = text + str(numbers[i][0]) + '-' + str(numbers[i][2]) + ' '
    print(f"Cidade# {count}:")
    print(text)
    print(f"Consumo medio: {total[1] / total[0] - 0.004:.2f} m3.")
    count += 1