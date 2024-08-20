while True:
    entry = int(input())
    if entry == 0:
        break
    numbers = []
    for i in range(1, entry + 1):
        numbers.append(str(i))
    print(" ".join(numbers))