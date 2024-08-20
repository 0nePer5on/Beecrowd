while True:
    entry = list(map(int, input().split()))
    if entry[0] <= 0 or entry[1] <= 0:
        break
    entry.sort()
    numbers = []
    txt = ""
    for i in range(entry[0], entry[1] + 1):
        numbers.append(i)
        txt = txt + str(i) + ' '
    print(f"{txt}Sum={sum(numbers)}")