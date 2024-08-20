num = int(input())
for i in range(num):
    entry = list(map(int, input().split()))
    if entry[0] % 2 == 0:
        entry[0] += 1
    total = 0
    for j in range(0, entry[1] * 2, 2):
        total += entry[0] + j
    print(total)