from operator import itemgetter
import math

count = 1
while True:
    num = int(input())
    if num == 0:
        break

    totalP, totalD = 0, 0
    numbers = dict()
    for n in range(num):
        P, D = map(int, input().split())
        totalP += P
        totalD += D
        if D // P in numbers:
            numbers[D//P] += P
        else:
            numbers[D//P] = P
    numList = sorted(list(numbers.keys()))
    text = ""
    for i in numList:
        text = text + str(numbers.get(i)) + '-' + str(i) + ' '
    print(f"Cidade# {count}:")
    print(text[0:len(text) - 1])
    print(f"Consumo medio: {math.floor((totalD * 100) / totalP) / 100:.2f} m3.")
    count += 1