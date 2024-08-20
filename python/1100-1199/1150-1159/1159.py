while True:
    entry = int(input())
    if entry == 0:
        break
    if entry % 2 == 1:
        entry += 1
    total = 0
    for i in range(0, 10, 2):
        total += entry + i
    print(total)