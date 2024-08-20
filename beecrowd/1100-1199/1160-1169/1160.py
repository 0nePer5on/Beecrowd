num = int(input())
for n in range(num):
    entry = list(map(float, input().split()))
    count = 0
    while True:
        if count > 100:
            print("Mais de 1 seculo.")
            break
        if entry[0] > entry[1]:
            print(f"{count} anos.")
            break
        count += 1
        entry[0] += int(entry[0] * (entry[2] / 100))
        entry[1] += int(entry[1] * (entry[3] / 100))