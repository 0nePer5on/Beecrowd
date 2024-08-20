while True:
    entry = list(map(int, input().split()))
    if entry[0] == 0:
        break
    num = (entry[0] * entry[1] * 100) // entry[2]
    print(int(num ** 0.5))